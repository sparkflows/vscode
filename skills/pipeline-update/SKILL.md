---
name: pipeline-update
description: Updates an existing Sparkflows pipeline from a natural language description. Use this skill whenever a user wants to modify, change, edit, or update an existing Sparkflows pipeline — for example "update pipeline 1234 to add an email notification after node 2" or "remove node 3 from pipeline 456 and connect node 1 to node 4". Requires a pipeline ID. Do NOT use this skill for creating new pipelines from scratch.
---

# Sparkflows Pipeline Updater

Fetches an existing Sparkflows pipeline by ID, applies the requested changes, and sends the updated pipeline back to the server.

## How updates are applied

Changes are always applied in this exact order to prevent structural conflicts:

1. **Remove edges** first — prevents dangling edges when nodes are removed
2. **Remove nodes** — safe once their edges are gone
3. **Add nodes** — inject new node JSON from the node library
4. **Add edges** — connect new and existing nodes

Never deviate from this order, even if the user describes changes in a different sequence.

## Node directory structure

Nodes are organized into the following category hierarchy. When searching for a node in the catalog, use this structure to locate the correct file path:

../pipeline-nodes/
├── 01-Branch/
├── 02-Code/
├── 03-EMR/
├── 04-EmptyOperator/
├── 05-LegoBlock/
├── 06-Sensor/
├── 07-TriggerNextDag/
├── 08-Workflow/
├── 09-Documentation/
├── 10-Configuration/
├── 11-Util/
├── 12-TriggerNextPipeline/
├── 13-Databricks/
├── 14-Snowflake/
└── 15-EMRServerless/

---

## Step-by-step process

**IMPORTANT** You MUST follow all the steps in order every time to update a pipeline. Do not skip steps or rearrange them. Each step builds on the previous ones to ensure the final output is correct and import-ready. For your internal reasoning, generate an initial plan from the steps.

The steps are:
1. Identify the pipeline ID
2. Confirm Airflow enabled/disabled (if disabled: assess request against available nodes, then either stop or proceed to step 3)
3. Fetch the pipeline JSON
4. Parse the update request
5. Load node resources (only if adding nodes)
6. Apply changes in order
7. Validate the updated pipeline
8. Save the updated pipeline
9. Import the updated pipeline (required)

Their detailed description are below:

### 1. Identify the pipeline ID

Scan the user's message for a pipeline ID. Accept it in any reasonable form: "pipeline 1234", "ID: 1234", "update 1234 to...".

If the pipeline ID is absent, ambiguous, or unclear — **stop and ask before doing anything else**:

> "Which pipeline would you like to update? Please provide the pipeline ID."

Do not proceed until you have a confirmed pipeline ID.

### 2. Confirm Airflow is enabled

> **HARD GATE — do not proceed to step 3 until this step is complete.**
>
> **Do not generate any pipeline JSON, load any node files, or assemble any output before this step is complete.** It does not matter that you could technically produce the JSON without server details — you must not. The Airflow check is mandatory and non-negotiable. No reasoning about being a "code assistant" or "generating the file directly" overrides this gate.

Ask the user for their Sparkflows server details:

> "Please provide your `fire_host_url` and `access_token` so I can verify Airflow is enabled on your server."

Once collected, run:

```bash
python .github/pipeline-references/isAirflowEnabled.py \
  --fire_host_url="<fire_host_url>" \
  --access_token="<access_token>"
```

**If the script returns "Airflow Enabled"** — record `fire_host_url` and `access_token` for reuse later, then proceed to step 3.

**If the script returns "Airflow Disabled"** — check whether the user's request involves adding new nodes:
- If the request is **only** removing nodes, removing edges, updating existing node fields, or adding edges between existing nodes — proceed to step 3. No new nodes are being introduced, so the Airflow restriction does not block the update.
- If the request involves **adding new nodes**, only two nodes are available: **Workflow** (`08-Workflow/workflow.json`) and **Trigger Next Pipeline** (`12-TriggerNextPipeline/triggerNextPipeline.json`). Assess whether the nodes to be added are limited to these two:
  - If not — stop and respond: "Airflow is disabled on your Sparkflows server. I cannot add those nodes to your pipeline."
  - If yes — proceed to step 3.

**If the script returns an error** — relay the error details to the user and stop.

### 3. Fetch the pipeline JSON

ALWAYS run the fetch script — **NEVER use a file that already exists in [fetched-pipelines](./fetched-pipelines/)**.
The cached file may be outdated. A fresh fetch is mandatory every time.

Ask the user for the following information:

| Parameter | Description | Default |
|---|---|---|
| `fire_host_url` | Full Sparkflows server URL | — |
| `access_token` | API access token | — |

Ask for all two in a single message — do not ask for them one at a time.

Once collected, run the fetch script. You should already have the pipeline ID from step 1, so include that as well:

```bash
  python .github/skills/pipeline-update/scripts/fetch_pipeline.py \
  --fire_host_url <fire_host_url> \
  --access_token <access_token> \
  --pipeline_id <pipeline_id> \
```

This stores the pipeline at [fetched-pipelines](./fetched-pipelines/) with the filename `<pipeline_id>.json`.

If the script returns a failure message, report it to the user and stop. If successful, read the full contents of [fetched-pipelines](./fetched-pipelines/) with the filename `<pipeline_id>.json` into context.

### 4. Parse the update request

Categorize each requested change into one or more of:

- **Edge removals** — disconnect nodes
- **Node removals** — remove a node entirely
- **Node additions** — add a new node from the node library
- **Edge additions** — connect nodes (new or existing)
- **Node parameter updates** — change a field value on an existing node

### 5. Load node resources (only if adding nodes)

Skip this step entirely if no new nodes are being added.

If new nodes are required:

1. Read [pipeline-node-index](../../pipeline-references/pipeline-node-index.md). This is a short file (~1–2 pages) that describes each node category in 2–3 lines. Use it to determine which catalog files are relevant to the user's request. Do not skip this step or go straight to a catalog — the index is what keeps token usage efficient.
2. Based on the index, load only the relevant catalog files from [pipeline-nodes-catalogs](../../pipeline-references/pipeline-nodes-catalogs/). Use the catalog entries to match each operation to the best available Sparkflows node.
4. If no compatible node exists for a required operation, stop and notify the user:
   > "No node compatible was found for `<operation>`. Please confirm the operation or choose a different approach."

   Never invent a node name or structure.

### 6. Apply changes in order

Work directly on the fetched pipeline JSON. Read [pipeline-schema](../../pipeline-references/pipeline-schema.md) before assembling — it defines the required field value formats, ID types, anchor rules, and positioning guidelines that must be followed exactly.

**Step A — Remove edges**
Delete every edge object from the `edges` array that the user wants removed. Match edges by their `source`, `target`, and/or anchor fields.

**Step B — Remove nodes**
Delete every node object from the `nodes` array that the user wants removed. All edges connected to removed nodes must have been deleted in Step A, if not, remove those edges.

**Step C — Add nodes**
Inject each new node's complete JSON file contents verbatim into the `nodes` array. Only set `id` and `x`/`y` during assembly — all other fields come from the node file unchanged. Position new nodes logically relative to their neighbors.

**Step D — Add edges**
Add new edge objects to the `edges` array. Use the next available sequential integer for the edge `id`. Include `sourceAnchor` or `targetAnchor` only when the node JSON defines named anchors.

**Step E — Update node parameters**
For any parameter changes on existing nodes, locate the correct field in the node's `fields` array and update its `value`. All values must remain strings per the field value format rules in [pipeline-schema](../../pipeline-references/pipeline-schema.md).

### 7. Validate the updated pipeline

Before saving, verify:
- [ ] No edges reference a node ID that no longer exists
- [ ] Every non-terminal node has at least one outgoing edge
- [ ] Every non-source node has at least one incoming edge
- [ ] All new node `id` values are unique strings
- [ ] All new edge `id` values are unique integers
- [ ] No `fields[].value` was converted from a string to a native JSON type
- [ ] Verify the JSON file is valid and well-formed

### 8. Save the updated pipeline

Overwrite the fetched pipeline file at [fetched-pipelines](./fetched-pipelines/) with the filename `<pipeline_id>.json` with the updated pipeline. The output must be a single valid JSON object with no markdown fences or embedded commentary.

Tell the user: `Pipeline <pipeline_id> updated and saved to .github/skills/pipeline-update/fetched-pipelines/<pipeline_id>.json`

### 9. Import the updated pipeline (required)

Always do this step — do not end your response after step 7.

Ask the user if they want to push the updated pipeline to the Sparkflows server. You should already have `fire_host_url` and `access_token` from step 2, and `pipeline_id` from step 1, so only ask for what is still missing:

| Parameter | Description | Default |
|---|---|---|
| `project_id` | Sparkflows project ID | — |

Once collected, run:

```bash
python .github/skills/pipeline-update/scripts/update_pipeline.py \
  --pipeline_json_path <path/to/pipeline.json> \
  --project_id <project_id> \
  --pipeline_id <pipeline_id> \
  --fire_host_url <fire_host_url> \
  --access_token <access_token>
```

Report success by saying ONLY "Pipeline updated successfully." or the exact error message.

---

## Example

**User input:**
> Update pipeline 1234 to:
> 1. Add an email notification after node 3
> 2. Remove node 2 and connect node 1 directly to node 3

**How to handle it:**
ID is `1234` → request `fire_host_url` and `access_token` → run `isAirflowEnabled.py` → Airflow is enabled, record credentials → fetch pipeline JSON → parse changes (adding a new node is required, so Airflow check matters) → remove edges connected to node 2 → remove node 2 → load pipeline node index → find EmailNotification node in utilities catalog → inject EmailNotification node → add edges (node 1→3, node 3→EmailNotification) → validate → save → offer import → run import script with `project_id` alongside already-known credentials → report success.

**Expected response:**
> "Please provide your `fire_host_url` and `access_token` so I can verify Airflow is enabled on your server."
> *(user provides credentials — Airflow is confirmed enabled)*
> Pipeline 1234 updated and saved to `.github/skills/pipeline-update/fetched-pipelines/1234.json`
>
> Would you like to push this update to your Sparkflows server? If so, please provide:
> - `project_id`
>
> Pipeline updated successfully.

---

## Constraints

- **Always require a pipeline ID.** Never fetch or modify a pipeline without a confirmed ID.
- **Always apply changes in order:** remove edges → remove nodes → add nodes → add edges → update parameters. Never deviate.
- **Always read [pipeline-schema](../../pipeline-references/pipeline-schema.md) before assembling.** It defines field value formats, ID type rules, and positioning — violations will break the import.
- **Never hallucinate a node.** If no catalog match exists for a new node, tell the user before proceeding.
- **Never modify node JSON structure.** Inject new node file contents verbatim. Only set `id`, `x`, and `y`.
- **Never reformat field values.** All `fields[].value` entries must remain strings. Never convert to a native JSON array, number, or boolean.
- **Always offer import after saving.** Step 8 is mandatory. Never end a response after step 7.
- **Never re-ask for `fire_host_url` or `access_token` in step 8.** Both are already collected in step 2 — reuse them directly.
- **Never store or log access tokens.** Use them only as script arguments.
- **Always fetch fresh.** Never skip the fetch script because a file already exists in [fetched-pipelines](./fetched-pipelines/). Cached files may be stale. Step 2 is mandatory every time.
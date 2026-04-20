---
name: workflow-update
description: Updates an existing Sparkflows workflow from a natural language description. Use this skill whenever a user wants to modify, change, edit, or update an existing Sparkflows workflow — for example "update workflow 1234 to add a filter after node 2" or "remove node 3 from workflow 456 and connect node 1 to node 4". Requires a workflow ID. Do NOT use this skill for creating new workflows from scratch.
---

# Sparkflows Workflow Updater

Fetches an existing Sparkflows workflow by ID, applies the requested changes, and sends the updated workflow back to the server.

## How updates are applied

Changes are always applied in this exact order to prevent structural conflicts:

1. **Remove edges** first — prevents dangling edges when nodes are removed
2. **Remove nodes** — safe once their edges are gone
3. **Add nodes** — inject new node JSON from the node library
4. **Add edges** — connect new and existing nodes

Never deviate from this order, even if the user describes changes in a different sequence.

## Node directory structure

Nodes are organized into the following category hierarchy. When searching for a node in the catalog, use this structure to locate the correct file path:

../nodes/
├── 01-Data-Connectors/
│   ├── 01-Input/
│   │   ├── 01-Database/
│   │   ├── 02-Structured-Files/
│   │   ├── 03-Unstructured-Files/
│   │   ├── 05-SFTP/
│   │   └── 06-Enterprise-Applications/
│   ├── 02-Output/
│   │   ├── 01-Database/
│   │   ├── 02-Structured-Files/
│   │   ├── 04-Streaming/
│   │   ├── 05-SFTP/
│   │   └── 06-Enterprise-Applications/
│   └── 03-Streaming/
│       ├── 01-Real-Time-Streaming/
│       └── 02-Structured-Streaming/
├── 02-Data-Profiling/
├── 03-Data-Preparation/
│   ├── 01-DateTime/
│   ├── 02-Math/
│   ├── 03-String/
│   ├── 04-Parsing/
│   ├── 05-Cleaning/
│   ├── 06-Add-Column/
│   ├── 06-Control-Structures/
│   ├── 07-Split/
│   ├── 08-Condition/
│   ├── 09-Cast-DataType/
│   ├── 10-Filter/
│   ├── 11-Join-Union/
│   ├── 12-Group/
│   ├── 13-Code/
│   └── 16-Others/
├── 04-Data-Validation/
├── 06-Data-Quality/
│   └── 01-Great-Expectations/
├── 07-Data-Visualization/
│   └── 01-SPC/
├── 08-Machine-Learning/
│   ├── 01-ML-Feature-Selection/
│   ├── 02-ML-SparkML/
│   │   ├── 02-FeatureScaler/
│   │   ├── 03-FeatureExtraction/
│   │   ├── 04-FeatureTransformers/
│   │   ├── 05-DimensionalityReduction/
│   │   ├── 06-FeatureSelection/
│   │   ├── 07-SplitDataset/
│   │   ├── 08-Clustering/
│   │   ├── 09-Regression/
│   │   ├── 10-Classification/
│   │   ├── 11-CollaborativeFiltering/
│   │   ├── 12-FreqPatternMining/
│   │   └── 13-Modeling/
│   ├── 03-ML-H2O/
│   ├── 05-ML-DeepLearning/
│   ├── 06-ML-Sklearn/
│   │   ├── Classification/
│   │   ├── Clustering/
│   │   ├── Data/
│   │   ├── Modeling/
│   │   ├── Optimization/
│   │   ├── PreProcessing/
│   │   └── Regression/
│   ├── 07-ML-Pycaret/
│   └── 08-ML-TimeSeries/
├── 09-Utilities/
│   ├── 01-Spark-Performance/
│   └── 02-Data-Partition/
├── 10-Documentation/
├── 11-Custom-Processors/
│   └── pyspark/
└── 13-Generative-AI/
├── 01-Hugging-Face/
├── 02-Ingestion/
├── 03-Vectorization/
├── 04-Retrieval/
└── 05-LLM-Inference/

---

## Step-by-step process

**IMPORTANT** You MUST follow all the steps in order every time to update a workflow. Do not skip steps or rearrange them. Each step builds on the previous ones to ensure the final output is correct and import-ready. For your internal reasoning, the generate an initial plan from the step.

The steps are:
1. Identify the workflow ID
2. Fetch the workflow JSON
   2b. Detect the workflow engine
3. Parse the update request
4. Load node resources (only if adding nodes)
5. Apply changes in order
6. Validate the updated workflow
7. Save the updated workflow
8. Import the updated workflow (required)

Their detailed description are below:

### 1. Identify the workflow ID

Scan the user's message for a workflow ID. Accept it in any reasonable form: "workflow 1234", "ID: 1234", "update 1234 to...".

If the workflow ID is absent, ambiguous, or unclear — **stop and ask before doing anything else**:

> "Which workflow would you like to update? Please provide the workflow ID."

Do not proceed until you have a confirmed workflow ID.

### 2. Fetch the workflow JSON

ALWAYS run the fetch script — **NEVER use a file that already exists in [fetched-workflows](./fetched-workflows/)**.
The cached file may be outdated. A fresh fetch is mandatory every time.

Ask the user for the following information:

| Parameter | Description | Default |
|---|---|---|
| `fire_host_url` | Full Sparkflows server URL | — |
| `access_token` | API access token | — |

Ask for all two in a single message — do not ask for them one at a time.

Once collected, run the fetch script. You should already have the workflow ID from step 1, so include that as well:

```bash
  python .github/skills/workflow-update/scripts/fetch_workflow.py \
  --fire_host_url <fire_host_url> \
  --access_token <access_token> \
  --workflow_id <workflow_id> \
```

This stores the workflow at [fetched-workflows](./fetched-workflows/) with the filename `<id>.json`.

If the script returns a failure message, report it to the user and stop. If successful, read the full contents of [fetched-workflows](./fetched-workflows/) with the filename `<id>.json` into context.

### 2b. Detect the workflow engine

Immediately after reading the fetched workflow JSON, inspect the root-level `engine` field:

| `engine` value | Meaning |
|---|---|
| `"scala"` | Workflow runs on Scala/Spark only |
| `"pyspark"` | Workflow runs on PySpark only |
| `"scala,pyspark"` or `"pyspark,scala"` | Workflow supports both engines |
| *(key absent)* | Treat as both engines — same as `"scala,pyspark"` |

Store this as the **workflow engine set** (e.g. `{scala}`, `{pyspark}`, or `{scala, pyspark}`). You will use it in step 4 to filter candidate nodes. Never proceed to add nodes without having determined the workflow engine set first.

### 3. Parse the update request

Categorize each requested change into one or more of:

- **Edge removals** — disconnect nodes
- **Node removals** — remove a node entirely
- **Node additions** — add a new node from the node library
- **Edge additions** — connect nodes (new or existing)
- **Node parameter updates** — change a field value on an existing node

### 4. Load node resources (only if adding nodes)

Skip this step entirely if no new nodes are being added.

If new nodes are required:

1. Read [node index](../references/node-index.md). This is a short file (~1–2 pages) that describes each node category in 2–3 lines. Use it to determine which catalog files are relevant to the user's request. Do not skip this step or go straight to a catalog — the index is what keeps token usage efficient.
2. Based on the index, load only the relevant catalog files from [catalogs](../references/catalogs/). Use the catalog entries to match each operation to the best available Sparkflows node.
3. **Engine filtering (mandatory):** For each candidate node identified from the catalog, load its `.json` file from the [nodes](../nodes/) directory and inspect its `engine` field at the root level of the node JSON. Apply the same interpretation rules as step 2b:
    - If the node's `engine` is `"scala"` → compatible only with scala workflows
    - If the node's `engine` is `"pyspark"` → compatible only with pyspark workflows
    - If the node's `engine` is `"scala,pyspark"` / `"pyspark,scala"` or is absent → compatible with both

   **Only select a node if its engine set intersects with the workflow engine set determined in step 2b.** If a candidate node is engine-incompatible, discard it and continue searching for a compatible alternative within the same catalog category. If multiple compatible nodes match the operation, prefer the one whose engine set is the most specific match to the workflow's engine.

4. If no compatible node exists for a required operation, stop and notify the user:
   > "No node compatible with the workflow's engine (`<engine>`) was found for `<operation>`. Please confirm the operation or choose a different approach."

   Never invent a node name or structure, and never use a node that is incompatible with the workflow's engine.

### 5. Apply changes in order

Work directly on the fetched workflow JSON. Read [workflow schema](../references/workflow-schema.md) before assembling — it defines the required field value formats, ID types, anchor rules, and positioning guidelines that must be followed exactly.

**Step A — Remove edges**
Delete every edge object from the `edges` array that the user wants removed. Match edges by their `source`, `target`, and/or anchor fields.

**Step B — Remove nodes**
Delete every node object from the `nodes` array that the user wants removed. All edges connected to removed nodes must have been deleted in Step A, if not, remove those edges.

**Step C — Add nodes**
Inject each new node's complete JSON file contents verbatim into the `nodes` array. Only set `id` and `x`/`y` during assembly — all other fields come from the node file unchanged. Position new nodes logically relative to their neighbors.

**Step D — Add edges**
Add new edge objects to the `edges` array. Use the next available sequential integer for the edge `id`. Include `sourceAnchor` or `targetAnchor` only when the node JSON defines named anchors.

**Step E — Update node parameters**
For any parameter changes on existing nodes, locate the correct field in the node's `fields` array and update its `value`. All values must remain strings per the field value format rules in [workflow schema](../references/workflow-schema.md).

### 6. Validate the updated workflow

Before saving, verify:
- [ ] No edges reference a node ID that no longer exists
- [ ] Every non-terminal node has at least one outgoing edge
- [ ] Every non-source node has at least one incoming edge
- [ ] All new node `id` values are unique strings
- [ ] All new edge `id` values are unique integers
- [ ] No `fields[].value` was converted from a string to a native JSON type
- [ ] Verify the JSON file is valid and well-formed

### 7. Save the updated workflow

Overwrite the fetched workflow file at [fetched-workflows](./fetched-workflows/) with the filename `<id>.json` with the updated workflow. The output must be a single valid JSON object with no markdown fences or embedded commentary.

Tell the user: `Workflow <id> updated and saved to .github/skills/workflow-update/fetched-workflows/<id>.json`

### 8. Import the updated workflow (required)

Always do this step — do not end your response after step 7.

Ask the user if they want to push the updated workflow to the Sparkflows server. Collect all five parameters in a single message. You should already have `fire_host_url`, `access_token`, `workflow_json_path`, and `project_id` from the previous steps, so just ask for the missing ones:

| Parameter | Description | Default |
|---|---|---|
| `project_id` | Sparkflows project ID | — |

Once collected, run:

```bash
python .github/skills/workflow-update/scripts/update_workflow.py \
  --workflow_json_path <path/to/workflow.json> \
  --project_id <project_id> \
  --workflow_id <workflow_id> \
  --fire_host_url <fire_host_url> \
  --access_token <access_token>
```

Report success by saying ONLY "Workflow updated successfully." or the exact error message.

---

## Example

**User input:**
> Update workflow 1234 to:
> 1. Print first 2 rows from output of node 4 as a new branch
> 2. Update node 1 to read from file 's3a://test'
> 3. Remove node 3 and connect node 1 to node 4
> 4. Remove node 2

**How to handle it:**
ID is `1234` → request parameters for fetch → fetch → read `engine` from workflow root (e.g. `"pyspark"` → engine set = `{pyspark}`) → parse changes → remove edges connected to nodes 2 and 3 → remove nodes 2 and 3 → find PrintNRows node in catalog, confirm its engine is compatible with `{pyspark}` → add PrintNRows node → update node 1's `path` field to `"s3a://test"` → add edges (node 1→4, node 4→PrintNRows) → validate → save → offer import.

**Expected response:**
> Workflow 1234 updated and saved to .github/skills/workflow-update/fetched-workflows/1234.json
>
> Would you like to push this update to your Sparkflows server? If so, please provide in a single message:
> - `fire_host_url`
> - `access_token`
> - `project_id`
> - `workflow_id`
> - `workflow_json`

---

## Constraints

- **Always require a workflow ID.** Never fetch or modify a workflow without a confirmed ID.
- **Always apply changes in order:** remove edges → remove nodes → add nodes → add edges → update parameters. Never deviate.
- **Always read [workflow schema](../references/workflow-schema.md) before assembling.** It defines field value formats, ID type rules, anchor handling, and positioning — violations will break the import.
- **Never hallucinate a node.** If no catalog match exists for a new node, tell the user before proceeding.
- **Never use an engine-incompatible node.** Always check the workflow's engine set (step 2b) before selecting any node. A node whose engine does not intersect the workflow's engine must never be added, regardless of how well it matches the operation. If no compatible node exists, stop and tell the user.
- **Never modify node JSON structure.** Inject new node file contents verbatim. Only set `id`, `x`, and `y`.
- **Never reformat field values.** All `fields[].value` entries must remain strings. Never convert to a native JSON array, number, or boolean.
- **Always offer import after saving.** Step 8 is mandatory. Never end a response after step 7.
- **Never store or log access tokens.** Use them only as script arguments.
- **Always fetch fresh.** Never skip the fetch script because a file already exists in
  [fetched-workflows](./fetched-workflows/) folder. Cached files may be stale. Step 2 is mandatory every time.
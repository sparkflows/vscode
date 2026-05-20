---
name: pipeline-creation
description: Generates import-ready Sparkflows pipeline JSON from a natural language description. A pipeline is an Airflow DAG that orchestrates execution — use this skill when a user wants to run or sequence multiple Sparkflows workflows (e.g. "create a pipeline that runs workflow A then workflow B"), or when the request involves EMR, EMR Serverless, Databricks, Snowflake, S3/EMR/Snowflake sensors, Bash/Python operators, pipeline triggers, email/SFTP/Azure utilities, or DAG configuration. If the user says "create a pipeline" or "run workflows in sequence/order", always use this skill — not workflow-creation. Only use this skill for creating new pipelines, not modifying existing ones.
---

# Sparkflows Pipeline Builder

Translates natural language pipeline descriptions into import-ready Sparkflows pipeline JSON by locating the correct node JSON files and injecting their full contents into the pipeline's `nodes` array.

## How pipeline JSON is assembled

A Sparkflows pipeline JSON has a `nodes` array and an `edges` array at its root. Each entry in `pipeline-nodes` is the **complete, unmodified JSON content** of a node file — loaded verbatim from the [pipeline-nodes](../../pipeline-nodes/) directory and inserted as-is. Edges are then defined separately to connect those nodes by their assigned IDs. The pipeline schema in [pipeline-schema](../../pipeline-references/pipeline-schema.md) defines all root-level keys and the exact edge format.

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

## Step-by-step process

**IMPORTANT** You MUST follow all the steps in order every time you generate a pipeline. Do not skip steps or rearrange them. Each step builds on the previous ones to ensure the final output is correct and import-ready. For your internal reasoning, generate an initial plan from the steps.

**There are no exceptions to the step order.** Do not reason your way around a HARD GATE. Do not treat yourself as a "code assistant that can just generate the file" — you are a pipeline builder that must validate prerequisites before producing any output. If a step requires user input, stop and ask. Do not proceed until the input is received.

The steps are:
1. Parse the request
2. Confirm Airflow enabled/disabled (if disabled: assess request against available nodes, then either stop or skip to step 5)
3. Load the node index
4. Load the relevant catalog files
5. Handle missing or unspecified parameters
6. Load the relevant node JSON files
7. Load the pipeline schema
8. Check an example pipeline
9. Model the DAG
10. Assign IDs
11. Assemble the pipeline JSON
12. Save and present
13. Import the pipeline

Their detailed description are below:

### 1. Parse the request

Read the user's pipeline description carefully. Identify:
- The sequence of operations (e.g., "create EMR cluster → run workflow → terminate cluster")
- Any explicit parameters (cluster configs, job IDs, SQL commands, S3 paths, DAG variables)
- Any **unspecified parameters** — note these now, you will handle them later in step 5

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

**If the script returns "Airflow Enabled"** — record `fire_host_url` and `access_token` for reuse in step 13, then proceed to step 3.

**If the script returns "Airflow Disabled"** — when Airflow is disabled, only two nodes are available: **Workflow** (`08-Workflow/workflow.json`) and **Trigger Next Pipeline** (`12-TriggerNextPipeline/triggerNextPipeline.json`). Assess the user's request from step 1 against these two nodes:
- If the request requires any functionality beyond these two nodes — stop and respond: "Airflow is disabled on your Sparkflows server. I cannot create your pipeline with the nodes available."
- If the request can be fulfilled using only these two nodes — skip steps 3 and 4 and proceed directly to step 5. The node files to load in step 6 are already known.

**If the script returns an error** — relay the error details to the user and stop.

### 3. Load the node index

> **HARD GATE — do not proceed to step 4 until this step is complete.**

Read [pipeline-node-index](../../pipeline-references/pipeline-node-index.md) in full. This is a short file (~1–2 pages) that describes each node category in 2–3 lines. Use it to determine which catalog files are relevant to the user's request.

**Forbidden shortcuts:**
- Do NOT guess category paths from node names or prior knowledge
- Do NOT jump directly to a catalog without reading the index first
  The index exists specifically to keep token usage efficient. Skipping it and scanning the nodes folder directly defeats this purpose and is never acceptable.

### 4. Load the relevant catalog files

> **HARD GATE — do not proceed to step 5 until this step is complete.**

Based on the index, load only the catalog files from [pipeline-nodes-catalogs](../../pipeline-references/pipeline-nodes-catalogs/) that cover the operations in the user's request. Use the catalog entries to match each operation to the best available Sparkflows node.

**Forbidden shortcuts:**
- Do NOT infer node file paths from node names without a catalog entry confirming the path
- Do NOT load catalogs not identified by the index in step 3
> If no node in any catalog matches a required operation, stop and notify the user immediately. Never invent a node name or structure.

### 5. Handle missing or unspecified parameters

Users will often describe a pipeline without specifying every detail — for example, "run a workflow on EMR" without providing a cluster config, or "send an email on completion" without providing an address. This is expected and fine.

Never block pipeline generation because a parameter is missing.

### 6. Load the relevant node JSON files

For each identified node, load its `.json` file from the [pipeline-nodes](../../pipeline-nodes/) directory using the path from the catalog. Only load the nodes you actually need. Do not load entire directories.

### 7. Load the pipeline schema

Read [pipeline-schema](../../pipeline-references/pipeline-schema.md) to confirm:
- The required root-level keys of the pipeline JSON
- The structure of the `nodes` array
- The format of the `edges` array and how nodes are referenced within it

### 8. Check an example pipeline

Open one file from [example-pipelines](../../pipeline-references/example-pipelines/) to verify how a complete pipeline looks when assembled — particularly how node JSON objects sit inside the `nodes` array and how edges reference them.

### 9. Model the DAG

Map out the directed acyclic graph of the pipeline:
- Order nodes by their logical sequence
- Identify every node-to-node connection
- Ensure every non-terminal node has at least one outgoing edge

### 10. Assign IDs

Generate unique IDs for each node and each edge. Be consistent — use sequential integers throughout.

### 11. Assemble the pipeline JSON

Build the final pipeline JSON:
- The `nodes` array contains the **complete JSON content of each node file**, injected verbatim, with the assigned `nodeId` applied
- The `edges` array is built from your DAG using the format defined in [pipeline-schema](../../pipeline-references/pipeline-schema.md)
- All other root-level keys come from the schema

Do not paraphrase, truncate, or restructure node JSON content. Inject it as loaded.

### 12. Save and present

Save the completed pipeline JSON to [outputs folder](./outputs/) with a filename like `pipeline-<uuid>.json` where `<uuid>` is a freshly generated UUID v4. After saving, tell the user the file path (ex: `Pipeline generated and saved to .github/skills/pipeline-creation/outputs/pipeline-1bd9f82c-28e1-41e1-882a-15e705a9086d.json`) and offer to import it into their Sparkflows server.

### 13. Import the pipeline (required)

Always do this step — do not end your response after step 12.

Ask the user if they want to import the pipeline into a Sparkflows server. Collect:

| Parameter | Description | Default |
|---|---|---|
| `fire_host_url` | Full Sparkflows server URL | — |
| `access_token` | API access token | — |
| `project_id` | Sparkflows project ID to import into | — |
| `uuid_option` | How to handle UUID conflicts | `createNewUUID` |

Ask for all four in a single message — do not ask for them one at a time.

Once collected, run:

```bash
python .github/skills/pipeline-creation/scripts/import_pipeline.py \
  --fire_host_url="<fire_host_url>" \
  --access_token="<access_token>" \
  --pipeline_json_path="<path to saved pipeline JSON>" \
  --project_id="<project_id>" \
  --uuid_option="<uuid_option>"
```

This will return either a success message with the **imported pipeline ID** or an error message with details.

Report success by saying ONLY "Pipeline with ID `<ID>` imported successfully." or the exact error message back to the user.

Record the returned pipeline ID in context for use later in the convrsation.

> `uuid_option` accepts two values:
> - `createNewUUID` — always generate a fresh UUID on import (default, safe for new pipelines)
> - `createNewUUIDIfExist` — only generate a new UUID if a pipeline with that UUID already exists

---

## Example

**User input:**
> Create a pipeline that:
> 1. Creates an EMR cluster
> 2. Runs a Sparkflows workflow on the cluster
> 3. Terminates the cluster when done

**How to handle it:**
Ask the user for `fire_host_url` and `access_token` → run `isAirflowEnabled.py` → Airflow is enabled, record credentials → load the pipeline node index → identify EMR and Workflow as relevant categories → load those two catalogs → match to `Create EMR JobFlow`, `EMR Workflow`, and `Terminate EMR JobFlow` → load their three JSON files → load the pipeline schema → check an example pipeline → assemble → save → run import script with `project_id` and `uuid_option` collected alongside the already-known credentials → report success or failure.

**Expected response:**
> "Please provide your `fire_host_url` and `access_token` so I can verify Airflow is enabled on your server."
> *(user provides credentials — Airflow is confirmed enabled)*
> Pipeline generated and saved to `.github/skills/pipeline-creation/outputs/pipeline-1bd9f82c-28e1-41e1-882a-15e705a9086d.json`
> Do you want to import this pipeline into your Sparkflows server? If so, please provide the following:
- `project_id`: The project ID to import into
- `uuid_option`: How to handle UUID conflicts (`createNewUUID` or `createNewUUIDIfExist`)
> Pipeline with ID `42` imported successfully.

---

## Constraints

- **Step 2 is mandatory before any generation.** Never produce pipeline JSON, load node files, or begin assembly before the Airflow check in step 2 is complete. No framing — "I'm a code assistant", "I can generate the file directly", "the user just wants the JSON" — overrides this.
- **New pipelines only.** This skill creates pipelines from scratch. Do not attempt to load, parse, or modify an existing pipeline JSON.
- **Never hallucinate a node.** If no catalog match exists, tell the user before proceeding.
- **Never modify node JSON structure.** Inject node file contents verbatim into the `nodes` array.
- **Never block on missing parameters.** If the user doesn't specify a parameter, that's fine — just generate the pipeline.
- **Output must be a single valid JSON file** with no markdown fences or commentary embedded within it.
- **Never store or log access tokens.** Use them only as arguments to scripts and do not echo them back in conversation after they are used.
- **Always offer import after saving.** Never end a pipeline creation response without completing step 13. Saving the JSON is not the final step.
- **Never re-ask for `fire_host_url` or `access_token` in step 13.** Both are already collected in step 2 — reuse them directly.
- **Never reformat field values.** Node `fields` entries store all values as strings — including arrays (`"[]"`) and booleans (`"true"`). When filling in user-specified values, serialize them into the same string format found in the node file. Never convert a string value to a native JSON array, number, or boolean.
---
name: workflow-creation
description: Generates import-ready Sparkflows workflow JSON from a natural language description. Use this skill whenever a user wants to build or prototype a new Sparkflows ETL pipeline, analytical model, or data processing flow — even if they just say something like "I want to load data from S3 and train a model" or "build me a pipeline that does X". Translates high-level intent into a fully structured workflow JSON with valid nodes, unique IDs, and correct edge connections that can be directly imported into Sparkflows. Only use this skill for creating new workflows, not modifying existing ones.
---

# Sparkflows Workflow Builder

Translates natural language workflow descriptions into import-ready Sparkflows workflow JSON by locating the correct node JSON files and injecting their full contents into the workflow's `nodes` array.

## How workflow JSON is assembled

A Sparkflows workflow JSON has a `nodes` array and an `edges` array at its root. Each entry in `nodes` is the **complete, unmodified JSON content** of a node file — loaded verbatim from the [nodes](../nodes/) directory and inserted as-is. Edges are then defined separately to connect those nodes by their assigned IDs. The workflow schema in [workflow schema](../references/workflow-schema.md) defines all root-level keys and the exact edge format.

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

## Step-by-step process

**IMPORTANT** You MUST follow all the steps in order every time you generate a workflow. Do not skip steps or rearrange them. Each step builds on the previous ones to ensure the final output is correct and import-ready. For your internal reasoning, the generate an initial plan from the step.

The steps are:
1. Parse the request
2. Confirm the engine type
3. Load the node index
4. Load the relevant catalog files
5. Handle missing or unspecified parameters
6. Load the relevant node JSON files
7. Load the workflow schema
8. Check an example workflow
9. Model the DAG
10. Assign IDs
11. Assemble the workflow JSON
12. Save and present
13. Import the workflow

Their detailed description are below:

### 1. Parse the request

Read the user's workflow description carefully. Identify:
- The sequence of operations (e.g., "read → filter → print")
- Any explicit parameters (file paths, column names, conditions, thresholds)
- Any **unspecified parameters** — note these now, you will handle them in step 4

### 2. Confirm the engine type

> **HARD GATE — do not proceed to step 3 until this step is complete.**

Ask the user which Spark engine their Sparkflows environment uses:

> "Which engine does your Sparkflows environment use — **Scala** or **PySpark**?"

Wait for the user's answer. Record the engine as either `scala` or `pyspark`. Do not assume an engine; always ask explicitly.

### 3. Load the node index

> **HARD GATE — do not proceed to step 4 until this step is complete.**

Read [node index](../references/node-index.md) in full. This is a short file (~1–2 pages) that describes each node category in 2–3 lines. Use it to determine which catalog files are relevant to the user's request.

**Forbidden shortcuts:**
- Do NOT guess category paths from node names or prior knowledge
- Do NOT jump directly to a catalog without reading the index first
  The index exists specifically to keep token usage efficient. Skipping it and scanning the nodes folder directly defeats this purpose and is never acceptable.

### 4. Load the relevant catalog files

> **HARD GATE — do not proceed to step 5 until this step is complete.**

Based on the index, load only the catalog files from [catalogs](../references/catalogs/) that cover the operations in the user's request. Use the catalog entries to match each operation to the best available Sparkflows node.

**Forbidden shortcuts:**
- Do NOT infer node file paths from node names without a catalog entry confirming the path
- Do NOT load catalogs not identified by the index in step 3
> If no node in any catalog matches a required operation, stop and notify the user immediately. Never invent a node name or structure.

### 5. Handle missing or unspecified parameters

Users will often describe a workflow without specifying every detail — for example, "read a CSV file" without providing a path, or "filter rows where x > 2000" without naming the dataset. This is expected and fine.

Never block workflow generation because a parameter is missing.

### 6. Load the relevant node JSON files

For each identified node, load its `.json` file from the [nodes](../nodes/) directory using the path from the catalog. Read the full file contents to check engine compatibility before injecting into the workflow.

**Engine filtering — apply this rule to every node before including it:**

Each node JSON may contain an `"engine"` key at the root level. Use the following compatibility rules based on the engine the user confirmed in step 2:

| `"engine"` value in node file | Compatible with `scala` | Compatible with `pyspark` |
|---|---|---|
| `"scala"` | Yes | No |
| `"pyspark"` | No | Yes |
| `"scala, pyspark"` | Yes | Yes |
| *(key absent)* | Yes | Yes |

- Only include a node if it is compatible with the user's selected engine.
- Nodes with no `"engine"` key are always compatible with both engines.

If the best-matched node for a required operation is **incompatible** with the user's engine, do not silently substitute an unrelated node. Instead:
1. Check whether an alternative node in the catalog satisfies the same operation and is engine-compatible.
2. If an alternative exists, use it.
3. If no compatible node exists, stop and tell the user: which operation has no compatible node for their selected engine.

Only load the nodes you actually need. Do not load entire directories.

### 7. Load the workflow schema

Read [workflow schema](../references/workflow-schema.md) to confirm:
- The required root-level keys of the workflow JSON
- The structure of the `nodes` array
- The format of the `edges` array and how nodes are referenced within it

### 8. Check an example workflow

Open one file from [workflow examples](../references/example-workflows/) to verify how a complete workflow looks when assembled — particularly how node JSON objects sit inside the `nodes` array and how edges reference them.

### 9. Model the DAG

Map out the directed acyclic graph of the workflow:
- Order nodes by their logical sequence
- Identify every node-to-node connection
- Ensure every non-terminal node has at least one outgoing edge

### 10. Assign IDs

Generate unique IDs for each node and each edge. Be consistent — use sequential integers throughout.

### 11. Assemble the workflow JSON

Build the final workflow JSON:
- The `nodes` array contains the **complete JSON content of each node file**, injected verbatim, with the assigned `nodeId` applied
- The `edges` array is built from your DAG using the format defined in [workflow schema](../references/workflow-schema.md)
- All other root-level keys come from the schema

Do not paraphrase, truncate, or restructure node JSON content. Inject it as loaded.

### 12. Save and present

Save the completed workflow JSON to [outputs folder](./outputs/) with a filename like `workflow-<uuid>.json` where `<uuid>` is a freshly generated UUID v4. After saving, tell the user the file path (ex: `Workflow generated and saved to .github/skills/workflow-creation/outputs/workflow-1bd9f82c-28e1-41e1-882a-15e705a9086d.json`) and offer to import it into their Sparkflows server.

### 13. Import the workflow (required)

Always do this step — do not end your response after step 12.

Ask the user if they want to import the workflow into a Sparkflows server. Collect:

| Parameter | Description | Default |
|---|---|---|
| `fire_host_url` | Full Sparkflows server URL | — |
| `access_token` | API access token | — |
| `project_id` | Sparkflows project ID to import into | — |
| `uuid_option` | How to handle UUID conflicts | `createNewUUID` |

Ask for all four in a single message — do not ask for them one at a time.

Once collected, run:

```bash
python .github/skills/workflow-creation/scripts/import_workflow.py \
  --fire_host_url="<fire_host_url>" \
  --access_token="<access_token>" \
  --workflow_json_path="<path to saved workflow JSON>" \
  --project_id="<project_id>" \
  --uuid_option="<uuid_option>"
```

Report success by saying ONLY "Workflow imported successfully." or the exact error message back to the user.

> `uuid_option` accepts two values:
> - `createNewUUID` — always generate a fresh UUID on import (default, safe for new workflows)
> - `createNewUUIDIfExist` — only generate a new UUID if a workflow with that UUID already exists

---

## Example

**User input:**
> Create a workflow that:
> 1. Reads a CSV file
> 2. Filters rows where `price > 42000` from step 1
> 3. Prints the first 10 rows from step 2

**How to handle it:**
Ask the user for their engine (Scala or PySpark) → load the node index → identify Data Connectors and Data Preparation as relevant categories → load those two catalogs → match to `Read CSV`, `RowFilter`, and `PrintNRows` → load their three JSON files and verify each is compatible with the user's engine → skip or substitute any incompatible node → load the schema → check an example → assemble → save → offer import → run import script with collected parameters → report success or failure.

**Expected response:**
> "Which engine does your Sparkflows environment use — Scala or PySpark?"
> *(user replies: PySpark)*
> Workflow generated and saved to .github/skills/workflow-creation/outputs/workflow-1bd9f82c-28e1-41e1-882a-15e705a9086d.json
> Do you want to import this workflow into your Sparkflows server? If so, please provide the following parameters in a single message:
- `fire_host_url`: Your Sparkflows server URL
- `access_token`: Your API access token
- `project_id`: The project ID to import into
- `uuid_option`: How to handle UUID conflicts (`createNewUUID` or `createNewUUIDIfExist`)
> Workflow imported successfully.

---

## Constraints

- **New workflows only.** This skill creates workflows from scratch. Do not attempt to load, parse, or modify an existing workflow JSON.
- **Never hallucinate a node.** If no catalog match exists, tell the user before proceeding.
- **Never modify node JSON structure.** Inject node file contents verbatim into the `nodes` array.
- **Never block on missing parameters.** If the user doesn't specify a parameter, that's fine — just generate the workflow.
- **Output must be a single valid JSON file** with no markdown fences or commentary embedded within it.
- **Never store or log access tokens.** Use them only as arguments to the import script and do not echo them back in conversation after the import runs.
- **Always offer import after saving.** Never end a workflow creation response without completing step 12. Saving the JSON is not the final step.
- **Never reformat field values.** Node `fields` entries store all values as strings — including arrays (`"[]"`) and booleans (`"true"`). When filling in user-specified values, serialize them into the same string format found in the node file. Never convert a string value to a native JSON array, number, or boolean.

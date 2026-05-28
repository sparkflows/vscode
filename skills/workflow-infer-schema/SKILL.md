---
name: workflow-infer-schema
description: 
  This skill infers the schema for nodes in a workflow JSON file by invoking `inferSchema.py`. It is **always called after** a Create Workflow or Update Workflow skill completes (i.e., once the workflow JSON has been generated or updated). It is never called in isolation — it is the final step of any create or update workflow operation.
---

## When to Trigger This Skill

| Preceding Skill     | Trigger Condition                                       |
|---------------------|---------------------------------------------------------|
| **Create Workflow** | Always call after the workflow JSON is generated        |
| **Update Workflow** | Always call after the updated workflow JSON is produced |

The infer schema skill reads context from the preceding skill's output (the workflow JSON) and from the user's original query to determine how to proceed.

---

## Step 0: Resolve Script Arguments

Before doing anything else, resolve all arguments required by `inferSchema.py`. Follow this order for each argument: **check conversation context first → if not found, ask the user**.

| Argument                | Flag                    | Required        | How to resolve                                                                                                          |
|-------------------------|-------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Workflow JSON file path | `--workflow_json_path`  | Always          | The preceding Create/Update Workflow skill will have produced this file. Use that path directly.                       |
| Host URL                | `--host_url`            | Always          | Look for a URL in the conversation (e.g. "https://..."). If not found, ask: *"What is the host URL?"*                  |
| Project ID              | `--project_id`          | Always          | Look for a project ID mentioned in the conversation. If not found, ask: *"What is the project ID?"*                   |
| Access token            | `--token`               | Always          | Look for a token or API key mentioned in the conversation. If not found, ask: *"What is your access token?"*          |
| Workflow ID             | `--workflow_id`         | Always          | Look for a workflow ID mentioned in the conversation. If not found, ask: *"What is the workflow ID?"*                 |
| Node IDs                | `--node_ids`            | Case 1 only     | Derived from the workflow JSON based on the user's query (see Case 1 below). Never required to ask directly.          |

**Collect all missing arguments in a single prompt** — do not ask for them one at a time. For example:
> "Before I run schema inference, I need a couple of details:
> - What is the host URL?
> - What is the workflow ID?"

Only proceed to the steps below once all required arguments are resolved.

---

## Skill Behavior

### Case 1: User Specified Node(s) for Schema Inference

The user's original query mentioned specific nodes or node types they want schema inferred for.

**Steps:**

1. **Load the workflow JSON** produced by the preceding Create/Update skill into context.

2. **Identify the relevant node IDs** from the workflow JSON that match what the user described. If the mapping is ambiguous or unclear, ask the user to clarify:
   > "I found multiple nodes that could match your description. Could you confirm which node IDs you'd like schema inferred for? Here are the candidates: [list node names and IDs]"

3. **Confirm with the user** before proceeding. Present the resolved nodes clearly:
   > "I will infer the schema for the following nodes:
   > - Read CSV (ID: 1)
   > - Read CSV (ID: 2)
   >
   > Shall I proceed?"

   **Do not move to step 4 until the user explicitly confirms.**

4. **Run the script** with all resolved arguments and the confirmed node IDs:
   ```bash
   python .github/skills/workflow-infer-schema/scripts/inferSchema.py \
     --workflow_json_path <path> \
     --node_ids <id1> <id2> ... \
     --host_url <host_url> \
     --project_id <project_id> \
     --token <token> \
     --workflow_id <workflow_id>
   ```

5. **Report the outcome** to the user — relay the script's success message or explain the failure and suggest next steps.

---

### Case 2: User Did Not Specify Nodes

The user's original query contained no information about which nodes to infer schema for.

**Steps:**

1. **Load the workflow JSON** produced by the preceding Create/Update skill into context.

2. **Ask the user:**
   > "Would you like me to automatically infer the schema for relevant nodes in your workflow?"

3. **If the user agrees**, run the script without `--node_ids` (the script will auto-detect qualifying starting nodes):
   ```bash
   python inferSchema.py \
     --workflow_json_path <path> \
     --host_url <host_url> \
     --project_id <project_id> \
     --token <token> \
     --workflow_id <workflow_id>
   ```

4. **If the user declines**, skip schema inference and inform the user they can run it later.

5. **Report the outcome** to the user — relay the script's success message or explain the failure and suggest next steps.

---

## Script Reference

**Script:** `inferSchema.py`

| Flag                   | Type             | Required        | Description                                              |
|------------------------|------------------|-----------------|----------------------------------------------------------|
| `--workflow_json_path` | string (path)    | Always          | Path to the workflow JSON file                           |
| `--host_url`           | string (URL)     | Always          | Base host URL for the API (e.g. `https://example.com`)  |
| `--project_id`         | integer          | Always          | Project ID                                               |
| `--token`              | string           | Always          | Access token passed in the request header                |
| `--workflow_id`        | integer          | Always          | Workflow ID used when calling `update_workflow.py`       |
| `--node_ids`           | string(s)        | Case 1 only     | Space-separated node IDs to infer schema for             |

**Script output:**
- Returns a **success** message on completion.
- Returns a **failure** message describing what went wrong.

Always surface the full script output to the user.

---

## Key Rules

- **Never skip this skill** after a Create or Update workflow operation — schema inference is always the final step.
- **Resolve all arguments before running the script** — never invoke `inferSchema.py` with missing required flags.
- **Collect all missing arguments in one prompt**, not one question at a time.
- **Never run the script before user confirmation** when specific nodes have been identified (Case 1, step 3).
- **Never guess node IDs** — always derive them from the workflow JSON. If ambiguous, ask the user.
- **The workflow JSON file path always comes from the preceding skill** — do not ask the user for it.
- If the script fails, report the error message verbatim and do not silently retry without informing the user.
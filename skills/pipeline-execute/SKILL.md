---
name: pipeline-execute
description: >
  Executes an existing Sparkflows pipeline by its name and project ID. Use this skill whenever a user wants to run or trigger a Sparkflows pipeline — for example "execute pipeline EMR_Workflow_Pipeline", "run pipeline foo in project 100063", or "trigger pipeline bar". Requires a pipeline name and project ID. Do NOT use this skill for creating,
  editing, or deleting pipelines.
---

# Sparkflows Pipeline Executor

Executes an existing Sparkflows pipeline via the POST `api/v1/executePipeline`
endpoint by calling [execute_pipeline.py](./scripts/execute_pipeline.py). On success,
automatically fetches and prints the execution result via [pipeline_execution_status.py](./scripts/pipeline_execution_status.py).

---

## Parameters

| Argument              | CLI Flag                  | Required | Type    | Description                                           |
|-----------------------|---------------------------|----------|---------|-------------------------------------------------------|
| Fire Host URL         | `--fire_host_url`         | ✅ Yes   | string  | Base URL of the Sparkflows instance                   |
| Access Token          | `--access_token`          | ✅ Yes   | string  | Auth token passed in the `token` header               |
| Pipeline Name         | `--pipeline_name`         | ✅ Yes   | string  | Name of the pipeline to execute                       |
| Project ID            | `--project_id`            | ✅ Yes   | integer | ID of the project the pipeline belongs to             |
| Email on Failure      | `--email_on_failure`      | ❌ No    | string  | Email address to notify if the pipeline fails         |
| Email on Success      | `--email_on_success`      | ❌ No    | string  | Email address to notify if the pipeline succeeds      |
| Lib Jars              | `--lib_jars`              | ❌ No    | string  | Comma-separated list of JAR paths to include          |
| Workflow Parameters   | `--workflow_parameters`   | ❌ No    | string  | Parameters passed to the pipeline                     |
| Spark Config          | `--spark_config`          | ❌ No    | string  | Additional Spark configuration key-value pairs        |

> Retrieve `--fire_host_url` and `--access_token` from context or ask the user for them if not available.

---

## Step-by-Step Process

Follow these steps **in order** every time. Do not skip or reorder steps.

### Step 1 — Collect the Pipeline Name, Project ID, and Required Parameters
Ask the user for the pipeline name and project ID they want to execute. Ask for `--fire_host_url` and
`--access_token` if not already available in the conversation context. Do not proceed
until all four values are obtained.

### Step 2 — Collect Optional Parameters
Always ask the user explicitly whether they want to configure each of the following optional parameters, even if they were not mentioned in the conversation:
- Email on Failure
- Email on Success
- Lib Jars
- Workflow Parameters
- Spark Config

Do not infer that the user does not want them based on context or prior messages. Wait for an explicit response before proceeding. If the user says no or skips a parameter, omit it entirely from the command. Do not pass empty strings for unused optional parameters.

### Step 3 — Run the Script
Execute [execute_pipeline.py](./scripts/execute_pipeline.py) with the collected arguments:

```bash
python .github/skills/pipeline-execute/scripts/execute_pipeline.py \
  --fire_host_url <FIRE_HOST_URL> \
  --access_token <ACCESS_TOKEN> \
  --pipeline_name <PIPELINE_NAME> \
  --project_id <PROJECT_ID> \
  [--email_on_failure <EMAIL>] \
  [--email_on_success <EMAIL>] \
  [--lib_jars <LIB_JARS>] \
  [--workflow_parameters <WORKFLOW_PARAMETERS>] \
  [--spark_config <SPARK_CONFIG>]
```

Only include optional flags if the user provided values for them.

### Step 4 — Report the Result

**On success:** The script prints `Pipeline {execution_id} executed` and then automatically
calls `pipeline_execution_status.py` to fetch and print the execution result in the format
`Execution Result: {description}`. Surface both pieces of information to the user.

**On failure:** Report the HTTP status code and JSON error message returned by
the script so the user can diagnose the issue.

---

## Behavior Notes

- The script POSTs to `/api/v1/executePipeline` with `pipelineName` and `projectId` as
  query parameters and a JSON body containing any provided optional fields (can be empty `{}`).
- On success, the API returns a single integer — the pipeline execution ID.
- After a successful execution, the script automatically invokes `pipeline_execution_status.py`
  with the returned execution ID to fetch the execution result.
- The script exits with code `1` on any HTTP error or exception, printing an error message to stdout.
- Optional parameters are only included in the request payload when explicitly
  provided — they are never sent as empty strings.

---

## Examples

### Minimal — name and project ID only
**User:** Run pipeline EMR_Workflow_Pipeline in project 100063.

**Command:**
```bash
python .github/skills/pipeline-execute/scripts/execute_pipeline.py \
  --fire_host_url http://sparkflows-host:8080 \
  --access_token <TOKEN> \
  --pipeline_name EMR_Workflow_Pipeline \
  --project_id 100063
```

**Response:**
```
Pipeline 4608 executed
Execution Result: Pipeline completed successfully
```

---

### With optional parameters
**User:** Execute pipeline EMR_Workflow_Pipeline in project 100063 and email me at ops@company.com if it fails.

**Command:**
```bash
python .github/skills/pipeline-execute/scripts/execute_pipeline.py \
  --fire_host_url http://sparkflows-host:8080 \
  --access_token <TOKEN> \
  --pipeline_name EMR_Workflow_Pipeline \
  --project_id 100063 \
  --email_on_failure ops@company.com
```

**Response:**
```
Pipeline 4609 executed
Execution Result: Pipeline completed successfully
```

---

## Constraints

- Do **not** use this skill to create, update, or delete pipelines.
- Do **not** pass empty strings for optional parameters — omit them entirely if not provided.

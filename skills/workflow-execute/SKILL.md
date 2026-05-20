---
name: workflow-execute
description: >
  Executes an existing Sparkflows workflow by its ID. Use this skill whenever
  a user wants to run or trigger a Sparkflows workflow — for example "execute
  workflow 1234", "run workflow 456", or "trigger workflow 789 and email me on
  failure". Requires a workflow ID. Do NOT use this skill for creating,
  editing, or deleting workflows.
---

# Sparkflows Workflow Executor

Executes an existing Sparkflows workflow via the POST `/api/v1/workflow/execute`
endpoint by calling [execute_workflow.py](./scripts/execute_workflow.py).

---

## Parameters

| Argument              | CLI Flag                | Required | Type    | Description                                      |
|-----------------------|-------------------------|----------|---------|--------------------------------------------------|
| Fire Host URL         | `--fire_host_url`       | ✅ Yes   | string  | Base URL of the Sparkflows instance              |
| Access Token          | `--access_token`        | ✅ Yes   | string  | Auth token passed in the `token` header          |
| Workflow ID           | `--workflow_id`         | ✅ Yes   | integer | ID of the workflow to execute                    |
| Email on Failure      | `--email_on_failure`    | ❌ No    | string  | Email address to notify if the workflow fails    |
| Email on Success      | `--email_on_success`    | ❌ No    | string  | Email address to notify if the workflow succeeds |
| Lib Jars              | `--lib_jars`            | ❌ No    | string  | Comma-separated list of JAR paths to include     |
| Program Parameters    | `--program_parameters`  | ❌ No    | string  | Parameters passed to the workflow program        |
| Spark Config          | `--spark_config`        | ❌ No    | string  | Additional Spark configuration key-value pairs   |

> Retrieve `--fire_host_url` and `--access_token` from context or ask the user for them if not available.

---

## Step-by-Step Process

Follow these steps **in order** every time. Do not skip or reorder steps.

### Step 1 — Collect the Workflow ID and Required Parameters
Ask the user for the workflow ID they want to execute. Ask for `--fire_host_url` and
`--access_token` if not already available in the conversation context. Do not proceed
until all three values are obtained.

### Step 2 — Collect Optional Parameters
Ask the user if they want to configure any optional parameters:
- Email on Failure
- Email on Success
- Lib Jars
- Program Parameters
- Spark Config

If the user says no or doesn't mention them, omit them entirely from the
command. Do not pass empty strings for unused optional parameters.

### Step 3 — Run the Script
Execute [execute_workflow.py](./scripts/execute_workflow.py) with the collected arguments:

```bash
python .github/skills/workflow-execute/scripts/execute_workflow.py \
  --fire_host_url <FIRE_HOST_URL> \
  --access_token <ACCESS_TOKEN> \
  --workflow_id <WORKFLOW_ID> \
  [--email_on_failure <EMAIL>] \
  [--email_on_success <EMAIL>] \
  [--lib_jars <LIB_JARS>] \
  [--program_parameters <PROGRAM_PARAMETERS>] \
  [--spark_config <SPARK_CONFIG>]
```

Only include optional flags if the user provided values for them.

### Step 4 — Report the Result

**On success:** Confirm the workflow was executed and surface any relevant
details from the response (e.g. execution ID, status, parameters used).

**On failure:** Report the HTTP status code and error message returned by
the script so the user can diagnose the issue.

---

## Behavior Notes

- The script POSTs to `/api/v1/workflow/execute` with a JSON body containing
  `workflowId` and any provided optional fields.
- The script exits with code `1` on any HTTP error or exception, printing an
  error message to stdout.
- Optional parameters are only included in the request payload when explicitly
  provided — they are never sent as empty strings.

---

## Examples

### Minimal — ID only
**User:** Run workflow 1234.

**Command:**
```bash
python .github/skills/workflow-execute/scripts/execute_workflow.py \
  --fire_host_url http://sparkflows-host:8080 \
  --access_token <TOKEN> \
  --workflow_id 1234
```

**Response:**
> Workflow 1234 executed successfully.
> Execution ID: 5678

---

### With optional parameters
**User:** Execute workflow 456 and email me at ops@company.com if it fails.

**Command:**
```bash
python .github/skills/workflow-execute/scripts/execute_workflow.py \
  --fire_host_url http://sparkflows-host:8080 \
  --access_token <TOKEN> \
  --workflow_id 456 \
  --email_on_failure ops@company.com
```

**Response:**
> Workflow 456 executed successfully with the following parameters:
> - Email on Failure: ops@company.com
>
> Execution ID: 7890

---

## Constraints

- Do **not** use this skill to create, update, or delete workflows.
- Do **not** pass empty strings for optional parameters — omit them entirely if not provided.
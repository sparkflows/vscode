---
name: workflow-delete
description: >
  Deletes an existing Sparkflows workflow by its ID. Use this skill whenever
  a user wants to remove a Sparkflows workflow — for example "delete workflow 1234".
  Requires a workflow ID. Do NOT use this skill for creating, editing, or executing workflows.
---

# Sparkflows Workflow Deleter

Deletes an existing Sparkflows workflow via the DELETE `/api/v1/workflows/id/{workflow_id}`
endpoint by calling [delete_workflow.py](./scripts/delete_workflow.py).

---

## Parameters

| Argument      | CLI Flag          | Required | Type    | Description                             |
|---------------|-------------------|----------|---------|-----------------------------------------|
| Fire Host URL | `--fire_host_url` | ✅ Yes   | string  | Base URL of the Sparkflows instance     |
| Access Token  | `--access_token`  | ✅ Yes   | string  | Auth token passed in the `token` header |
| Workflow ID   | `--workflow_id`   | ✅ Yes   | integer | ID of the workflow to delete            |

> Retrieve `--fire_host_url` and `--access_token` from context or ask the user if not available.

---

## Step-by-Step Process

Follow these steps **in order** every time. Do not skip or reorder steps.

### Step 1 — Collect Parameters

Ask the user for the workflow ID they want to delete. Ask for `--fire_host_url` and
`--access_token` if not already available in the conversation context. Do not proceed
until all three values are obtained.

### Step 2 — Confirm Deletion

Ask the user to confirm the deletion with a yes/no question (e.g., *"Are you sure you
want to delete workflow 1234?"*). If the user says no, cancel
the operation and do not run the script.

### Step 3 — Run the Script

```bash
python .github/skills/workflow-delete/scripts/delete_workflow.py \
  --fire_host_url <FIRE_HOST_URL> \
  --access_token <ACCESS_TOKEN> \
  --workflow_id <WORKFLOW_ID>
```

### Step 4 — Report the Result

**On success:** Confirm the workflow was deleted and surface any relevant details from
the response (e.g. deletion status, workflow ID).

**On failure:** Report the HTTP status code and error message returned by the script
so the user can diagnose the issue.

---

## Behavior Notes

- The script sends a DELETE request to `/api/v1/workflows/id/{workflow_id}`.
- The workflow ID is passed as a **path parameter** — there is no request body.
- The auth token is sent in the `token` request header.
- The script exits with code `1` on any HTTP error or exception, printing an error
  message to stdout.

---

## Examples

**User:** Delete workflow 1234.

**Command:**
```bash
python .github/skills/workflow-delete/scripts/delete_workflow.py \
  --fire_host_url http://sparkflows-host:8080 \
  --access_token <TOKEN> \
  --workflow_id 1234
```

**Response:**
> Workflow 1234 deleted successfully.

---

## Constraints

- Do **not** use this skill to create, update, or execute workflows.
# 

# Workflow Assistant: User Guide

A VS Code Copilot skill that creates and updates Sparkflows workflows from plain English descriptions.


## **Prerequisites**

- **Python 3.8+** —[ ](https://www.python.org/downloads/)[download here](https://www.python.org/downloads/)

`requests` **library** : \
 pip install requests

- **GitHub Copilot** extension installed and signed in to VS Code

- **A running Sparkflows server** with your:

- Server URL — e.g. `https://your-sparkflows-server.com`

- Access token — found in Sparkflows under **Administration → My Account → Generate Token**


## **Installation**

https://github.com/user-attachments/assets/c6226e20-98e5-4daf-afce-9467cc7cd572

## **Folder structure**

Do not edit anything inside `.github/`. These are the node library and schema files the assistant reads automatically.


## **How to use**

Open Copilot Chat in VS Code with `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac), then type your request naturally. VS Code picks the right skill automatically based on what you ask.

### **Creating a new workflow**

Describe what the workflow should do:

"Create a workflow that reads a CSV file, filters rows where price is greater than 5000, and saves the result as a Parquet file."

"Build a PySpark pipeline that reads from a JDBC connection, removes duplicates, runs a random forest classifier, and writes the output to Snowflake."

The assistant will:

1. Match your description to nodes from the library

2. Build a valid workflow JSON

3. Save it to `outputs/`

4. Ask for your server details and import it

### **Updating an existing workflow**

Always include the workflow ID in your request:

"Update workflow 1234 — add a filter node after node 2 and connect it to node 3."

"In workflow 5678, remove node 4 and update node 1 to read from `s3a://my-bucket/data.csv`."

The assistant will:

1. Fetch the current workflow from your server

2. Apply your changes

3. Validate the result

4. Push the updated workflow back


## **Providing credentials**

The first time you run a create or update in a session, the assistant will ask for:

| What | Example |
|---|---|
| Server URL | https://your-sparkflows-server.com |
| Access token | eyJhbGci... |
| Project ID | 1 |
| uuid_option | CreateNewUUID or  |

Provide all of them in a single message or as prompted.

## **Outputs**

| Operation | Output location |
|---|---|
| Create | outputs/workflow-<uuid>.json |
| Update | fetched-workflows/<workflow-id>.json |

Both folders sit at the repo root and are fully visible in VS Code Explorer and your local file browser (Finder/Explorer).


## **Troubleshooting**

| Problem | Fix |
|---|---|
| Skills not showing under Workspace | Make sure VS Code is opened at the repo root, not inside a subfolder |
| "Access Token is not valid" | Regenerate your token in Sparkflows under Administration → My Account |
| "Host URL is not valid" | Ensure the URL starts with https:// and has no trailing slash |
| Copilot picks the wrong skill | Be explicit — say "create a new workflow" or "update workflow 1234" |


## **Security**

Access tokens are passed only as script arguments at runtime and are never written to any output file. **Do not commit tokens to Git.**

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

**1. Clone the repository**

Unzip the given files

OR

 git clone [https://github.com/](https://github.com/your-org/sparkflows-workflow-assistant.git)…

**2. Open the folder in VS Code**

File → Open Folder → select sparkflows-workflow-assistant

**3. Trust the workspace when prompted**

VS Code will show a trust dialog on first open. Click **Yes, I trust the authors** to enable all features including Copilot skill execution.

<img width="468" height="290" alt="image" src="https://github.com/user-attachments/assets/27a5fbfa-159a-4d9e-9339-09a681812831" />


Note: Agent Skills seems to work best with Claude Models.

**1. Download Agent Skill files**

Unzip the file or clone the repo to gain access to 4 folders: “nodes”, “references”, “workflow-creation” and “workflow-update”

**2. Open your VS Code Project**

Open the workspace you want to add the Agent Skills to. You can add the Agent Skills to an existing workspace you are currently working in or to a completely new vscode workspace.

*Note:* Make sure you open the project at its root directory. 

The below instructions install the Sparkflows Agent Skills on a completely new vscode workspace.

**3. Verify you have all prerequisites**

You should have 2 things:

1. The unzipped or cloned Sparkflows Agent Skill files

2. Your opened VS Code Workspace/Project

<img width="511" height="304" alt="image" src="https://github.com/user-attachments/assets/f8710f86-9b39-4cce-baf5-72bc217524d1" />


**<span style="text - decoration: underline;">NOTE:**</span> Skip steps 4-10 below if you already have “.github/skills” at the root of your project. This means you already have the file structure for Agent Skills set up for your project. 

**4. Open Copilot Chat**

From within your VS Code project, open Copilot Chat (Top middle chat icon)

<img width="511" height="305" alt="image" src="https://github.com/user-attachments/assets/86ccd7f5-e447-4e46-9a78-f96ae4e474ce" />


**5. Open Copilot Settings** 

Click the gear icon

<img width="512" height="307" alt="image" src="https://github.com/user-attachments/assets/a428e8bd-2eb6-459d-978e-b93eb9796923" />


**6. Generate Skill**

Click the down arrow next to “Generate Skill” and select “New Skill (Workspace)”

<img width="512" height="306" alt="image" src="https://github.com/user-attachments/assets/145e6912-3605-4b43-846d-032332498b30" />


**7. Select Directory**

Select “.github” as the directory

<img width="511" height="303" alt="image" src="https://github.com/user-attachments/assets/0315bfc7-ce45-4846-b4b8-7a9fe8867674" />


**8. Add Temporary Skill Name**

Add a temporary name for the skill.

*Note:* This skill will be replaced later, this is required to set up the copilot skills directory structure. 

<img width="509" height="303" alt="image" src="https://github.com/user-attachments/assets/dde97be1-f50c-43ec-b153-26b6c03f6afa" />


**9. Verify Agent Skills Directory Structure**

Exit out of the customizations window and you should see a .github folder created with subfolders .github/skills/temp/[SKILL.md](SKILL.md)

<img width="511" height="301" alt="image" src="https://github.com/user-attachments/assets/38a28665-b21e-441f-90db-6170cd250163" />


**10. Delete Temporary Skill**

Delete the “temp” folder (this should also delete all its contents).

**11. Add Sparkflows Agent Skills**

Drag and drop the “nodes”, “references”, “workflow-creation”, and “workflow-update” folders into the “skills” folder.

<img width="511" height="304" alt="image" src="https://github.com/user-attachments/assets/6c6e93ba-cc11-4a40-b5e2-026b8c129ea6" />


**12. Verify Agent Skill Directory**

Your .github folder should now look as follows:

<img width="511" height="305" alt="image" src="https://github.com/user-attachments/assets/ef6f379d-001d-4251-a68e-679fb795b502" />


**13. Verify Copilot Detects Sparkflows Skills**

Open the Copilot settings as before (Gear Icon). Under the skills tab you should see “workflow-creation” and “workflow-update” under Workspace skills

<img width="509" height="303" alt="image" src="https://github.com/user-attachments/assets/a67342be-5594-43e9-b14e-1e26059f19d3" />



**4. Verify skills are loaded**

Open the Agent Customizations panel:

- Click the Copilot icon in the top right of the chat panel

- Select **Skills**

- Under **Workspace** you should see both skills listed:

- `workflow-creation` — Generates import-ready Sparkflows workflow JSON

- `workflow-update` — Updates an existing Sparkflows workflow

If both appear, you are ready to use the assistant.

<img width="468" height="547" alt="image" src="https://github.com/user-attachments/assets/2e2d38a5-2497-4d36-9da7-df69c49645f6" />



## **Folder structure**

sparkflows-assistant/

<img width="468" height="598" alt="image" src="https://github.com/user-attachments/assets/5b9df79b-ae72-4842-86be-2617cc9ec383" />


Do not edit anything inside `.github/skills/nodes/` or `.github/skills/references/`. These are the node library and schema files the assistant reads automatically.


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

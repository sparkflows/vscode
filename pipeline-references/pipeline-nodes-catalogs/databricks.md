# Databricks Nodes

## Cluster Management
- **Create Cluster** `13-Databricks/createCluster.json` — This node creates a new Cluster in Databricks by using details in configuration and passes the cluster ID to the next step.
- **Terminate Cluster** `13-Databricks/terminateCluster.json` — This node terminates Cluster in Databricks.

## Job Execution
- **Run Notebook** `13-Databricks/submitJob.json` — This node use to submit a new Databricks job to Cluster by using details in configuration
- **Run Job** `13-Databricks/runNow.json` — This node use to trigger a run of an existing Databricks job to Cluster by using details in configuration
- **Run Workflow** `13-Databricks/executeWorkflow.json` — This node adds the workflow in the project as an databricks step and executes it.

# EMR Nodes

## Classic EMR
- **Create EMR JobFlow** `03-EMR/emr.json` — This node creates a new EMR JobFlow by using details in configuration and passes the EMR ID to the next step.
- **Add Step EMR JobFlow** `03-EMR/addStep.json` — This node adds steps to an existing EMR job flow and executes the arguments as one command using command-runner.jar
- **Terminate EMR JobFlow** `03-EMR/emrTerminate.json` — This node terminates the EMR JobFlow.
- **EMR Workflow** `03-EMR/emrWorkflow.json` — This node adds the workflow in the project as an EMR step and executes it.

## EMR Serverless
- **Create EMR Serverless Application** `15-EMRServerless/EmrServerlessCreateApplication.json` — This node creates a new EMR Serverless Application.
- **Start EMR Serverless Job** `15-EMRServerless/EmrServerlessStartJob.json` — This node can be use to start an EMR Serverless Job.
- **Stop EMR Serverless Application** `15-EMRServerless/EmrServerlessStopApplication.json` — This node Stops the EMR Serverless Application.
- **Delete EMR Serverless Application** `15-EMRServerless/EmrServerlessDeleteApplication.json` — This node Deletes the EMR Serverless Application.
- **EMR Serverless Workflow** `15-EMRServerless/EmrServerlessWorkflow.json` — This node adds the workflow in the project as an EMR Serverless application step and executes it.

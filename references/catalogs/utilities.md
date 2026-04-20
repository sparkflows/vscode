# Utilities Nodes

## General
- **InlineDQ_Validation** `09-Utilities/InlineDQ_Validation.json` — Node to perform InlineDQ validation and generate pass/fail result.
- **CodeLibrary** `09-Utilities/codelibrary.json` — This node have code library.
- **Pdf Attachments from Emails** `09-Utilities/download_pdf_attachments.json` — This node reads emails and download Pdf Attachments from all provided email addresses.
- **EmailNotification** `09-Utilities/emailNotification.json` — This node sends notification to given email address with given content.
- **ML Data Metrics** `09-Utilities/node_ml_model_metrics.json` — This node calculates and outputs feature statistics and data drift metrics-including PSI and drift flags-by comparing a baseline dataset with a new batch dataset.
- **Generate Dynamic Parameters** `09-Utilities/nodegenerateparameters.json` — This node create dynamic parameters for each column and value.
- **Generate Pipeline Parameters** `09-Utilities/nodegeneratepipelineparameter.json` — This node create pipeline parameters for each column and value.
- **Rest API Client** `09-Utilities/noderestapiclient.json` — Rest API Client node create the dataframe from the json response.
- **PGPDecrypt** `09-Utilities/pgpdecrypt.json` — Decrypt the PGP files and upload to target location.
- **ExecuteRedshiftStatement** `09-Utilities/redshiftstmt.json` — This node executes the Redshift statement.

## Spark Performance
- **Cache Data Frame** `09-Utilities/01-Spark-Performance/cachedataframe.json` — Caches the DataFrame with the provided StorageLevel.
- **Print Spark Configuration** `09-Utilities/01-Spark-Performance/sparkconfigrations.json` — Print the all spark configuration used in workflow.
- **Unpersist DataFrame** `09-Utilities/01-Spark-Performance/unpersistdataframe.json` — Unpersists the output DataFrames of the given Nodes.

## Data Partition
- **Coalesce** `09-Utilities/02-Data-Partition/coalesce.json` — This node coalesces the DataFrame into specified number of Partitions.
- **Number Of Partitions** `09-Utilities/02-Data-Partition/numberofpartitions.json` — This node will get the number of partitions in input dataframe.
- **Repartition** `09-Utilities/02-Data-Partition/repartition.json` — This node repartitions incoming dataframe into a specified number of partitions.

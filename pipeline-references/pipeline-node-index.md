# Sparkflows Pipeline Node Index

## How to use this index
Identify which categories are relevant to the pipeline, then load only those catalog files
from [pipeline-nodes-catalogs](./pipeline-nodes-catalogs/). Most pipelines need 2–4 categories.

---

## EMR `pipeline-nodes-catalogs/emr.md`
Nodes for creating, managing, and executing Classic EMR JobFlows and EMR Serverless applications.
Covers cluster creation, adding steps, running workflows, and termination. Use for any pipeline
that orchestrates EMR-based Spark or Hadoop jobs.

## Databricks `pipeline-nodes-catalogs/databricks.md`
Nodes for managing Databricks clusters and triggering job execution. Covers cluster creation
and termination, notebook submission, job runs, and workflow execution. Use for any pipeline
that orchestrates Databricks workloads.

## Snowflake `pipeline-nodes-catalogs/snowflake.md`
Nodes for running SQL commands and monitoring data state in Snowflake. Use when the pipeline
needs to execute Snowflake queries or wait for a Snowflake condition to be met.

## Sensors `pipeline-nodes-catalogs/sensors.md`
Polling nodes that wait for external state to reach a target condition. Covers S3 key presence,
EMR JobFlow and step completion, and EMR Serverless application/job states. Use when a pipeline
step must block until an upstream resource or job reaches a desired state.

## Code `pipeline-nodes-catalogs/code.md`
Nodes for executing arbitrary code within the pipeline. Covers Bash scripts, Python callables,
and conditional branching via a Python return value. Use when no higher-level node covers the
required logic.

## Triggers `pipeline-nodes-catalogs/triggers.md`
Nodes for chaining pipeline execution. Covers triggering another DAG, triggering the next
pipeline in a sequence, and embedding a Sparkflows workflow as a pipeline step. Use when one
pipeline needs to kick off another pipeline or workflow.

## Utilities `pipeline-nodes-catalogs/utilities.md`
General-purpose operational nodes. Covers email notifications, metrics publishing, SFTP file
transfer, Azure Function invocation, inline data quality validation, empty operator placeholders,
and sticky notes. Use for cross-cutting concerns like alerting, monitoring, and documentation.

## Configuration `pipeline-nodes-catalogs/configuration.md`
Nodes for injecting runtime configuration into the DAG. Covers DAG arguments, DAG variables,
and YAML configuration files. Use at the start of a pipeline to set up parameters consumed by
downstream nodes.

## Lego Blocks `pipeline-nodes-catalogs/lego-blocks.md`
Reusable custom block nodes that wrap specific processing logic. Covers XML parsing, mapping
language execution, and project-specific transform blocks. Use when a pre-built encapsulated
block covers the required transformation.

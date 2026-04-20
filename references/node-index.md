# Sparkflows Node Index

## How to use this index
Identify which categories are relevant to the workflow, then load only those catalog files
from `references/catalogs/`. Most workflows need 2–4 categories.

---

## 01 · Data Connectors `catalogs/data-connectors.md`
Nodes for reading and writing data. Covers databases (JDBC, Hive, etc.), structured files
(CSV, Parquet, JSON, Avro, Excel), unstructured files, SFTP, enterprise apps (Salesforce,
SAP), and streaming (Kafka, Kinesis). Use for any ingestion or export node.

## 02 · Data Profiling `catalogs/data-profiling.md`
Summary statistics, schema inference, null counts, distribution analysis. Use when the
workflow includes an EDA or data quality inspection step.

## 03 · Data Preparation `catalogs/data-preparation.md`
The largest category. Covers filtering, joining, grouping, string/math/datetime ops,
casting, cleaning, splitting, conditional logic, and code nodes (SQL, PySpark). Use for
any transformation or reshaping step.

## 04 · Data Validation `catalogs/data-validation.md`
Schema checks, constraint enforcement, row-level assertion testing. Use when the workflow
needs to validate data against rules before proceeding.

## 06 · Data Quality `catalogs/data-quality.md`
Great Expectations integration nodes. Use for expectation suites and quality reports.

## 07 · Data Visualization `catalogs/data-visualization.md`
Chart and SPC (Statistical Process Control) nodes. Use when the workflow produces visual
output or monitoring charts.

## 08 · Machine Learning `catalogs/machine-learning.md`
SparkML, H2O, Sklearn, Pycaret, DeepLearning, and TimeSeries nodes. Covers feature
engineering, model training, evaluation, and scoring across all supported frameworks.

## 09 · Utilities `catalogs/utilities.md`
Spark performance tuning and data partitioning nodes. Use when the workflow needs
caching, repartitioning, or broadcast hints.

## 11 · Custom Processors `catalogs/custom-processors.md`
PySpark custom script nodes. Use when no standard node covers the required logic.

## 13 · Generative AI `catalogs/generative-ai.md`
Hugging Face, embedding/vectorization, retrieval, and LLM inference nodes. Use for any
RAG pipeline or LLM-powered workflow step.
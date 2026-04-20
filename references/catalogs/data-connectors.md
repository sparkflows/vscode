# Data Connectors Nodes

## Database
- **Execute BigQuery** `01-Data-Connectors/01-Input/01-Database/executeBigQuery.json` — It executes the query in BigQuery and creates a DataFrame from it.
- **Execute CRUD Stmt In Snowflake** `01-Data-Connectors/01-Input/01-Database/executeCURDStmtInSnowflake.json` — This node executes Stored Procedure in Snowflake.
- **Execute Query In Snowflake** `01-Data-Connectors/01-Input/01-Database/executeQueryInSnowFlake.json` — This node executes query in Snowflake.
- **Execute Stored Procedure In Snowflake** `01-Data-Connectors/01-Input/01-Database/executesnowflakestoredprocedure.json` — This node executes Stored Procedure in Snowflake.
- **Hive Incremental** `01-Data-Connectors/01-Input/01-Database/hiveIncremental.json` — This node is used to incrementally read data from Hive table.
- **Read JDBC** `01-Data-Connectors/01-Input/01-Database/jdbcConnection.json` — This node reads data from Relational Databases using JDBC and creates a DataFrame from it.
- **JDBC Incremental Load** `01-Data-Connectors/01-Input/01-Database/jdbcincrementalload.json` — This node is used to load incremental data from RDBMS to Hive.
- **Read Netsuite** `01-Data-Connectors/01-Input/01-Database/netsuiteConnection.json` — This node reads data from Oracle Netsuite using token based authentication and creates a DataFrame from it.
- **Netsuite AutoIncrement** `01-Data-Connectors/01-Input/01-Database/netsuite_incremental.json` — This node reads incremental data from Oracle Netsuite using token based authentication and creates a DataFrame from it.
- **AutoIncrement** `01-Data-Connectors/01-Input/01-Database/nodeAutoIncrement.json` — This node reads data from Relational Databases using JDBC and creates a DataFrame from it.
- **DB Incremental Ingestion** `01-Data-Connectors/01-Input/01-Database/nodeDbIncrementalIngestion.json` — This node incrementally fetches data from a database table based on a key column (DATE, ID, or TIMESTAMP).
- **Read JDBC** `01-Data-Connectors/01-Input/01-Database/pyspark_read_jdbc.json` — This node writes data to databases using JDBC.
- **Query JDBC** `01-Data-Connectors/01-Input/01-Database/queryJdbcConnection.json` — This node executes query on Relational Databases using JDBC and creates a DataFrame from it.
- **Read BigQuery** `01-Data-Connectors/01-Input/01-Database/readBigquery.json` — It reads data from BigQuery table and creates a DataFrame from it.
- **Read Cassandra** `01-Data-Connectors/01-Input/01-Database/readCassandra.json` — This node reads data from Apache Cassandra.
- **Read DynamoDB** `01-Data-Connectors/01-Input/01-Database/readDynamoDB.json` — This node reads data from DynamoDB and gets the credentials from the instance profile.
- **Read From Snowflake** `01-Data-Connectors/01-Input/01-Database/readFromSnowFlake.json` — This node reads a table from Snowflake.
- **Read Iceberg** `01-Data-Connectors/01-Input/01-Database/readIcebergTable.json` — It reads data from Iceberg table and creates a DataFrame from it.
- **Read Incorta** `01-Data-Connectors/01-Input/01-Database/read_incorta.json` — Reads data using the Read Incorta connector.
- **Read Databricks Table** `01-Data-Connectors/01-Input/01-Database/readdatabrickstable.json` — This node reads a table from Databricks.
- **Read Elastic Search** `01-Data-Connectors/01-Input/01-Database/readelasticsearch.json` — Reads data from ElasticSearch.
- **Read HIVE Table** `01-Data-Connectors/01-Input/01-Database/readhivetable.json` — This node reads data from Apache HIVE table and creates a DataFrame from it.
- **Read MongoDB** `01-Data-Connectors/01-Input/01-Database/readmongodb.json` — Reads data from MongoDB.

## Structured Files
- **Read Avro** `01-Data-Connectors/01-Input/02-Structured-Files/avro.json` — Dataset Node for Reading Apache Avro Files.
- **Create Dataset** `01-Data-Connectors/01-Input/02-Structured-Files/createdataset.json` — Creates a dataset with the specified number of rows and nine pre-defined columns.
- **Read CSV** `01-Data-Connectors/01-Input/02-Structured-Files/csv.json` — It reads in CSV files and creates a DataFrame from it.
- **Read Delta** `01-Data-Connectors/01-Input/02-Structured-Files/delta.json` — Dataset Node for reading Apache Delta files.
- **Empty Dataset** `01-Data-Connectors/01-Input/02-Structured-Files/empty.json` — It creates an empty DataFrame.
- **Read Excel** `01-Data-Connectors/01-Input/02-Structured-Files/excel.json` — Dataset Node for Reading Excel Files.
- **Read Excel Advanced** `01-Data-Connectors/01-Input/02-Structured-Files/excel_advanced.json` — Advanced Excel Reader Node – Load one or more sheets, named ranges, or specific cell ranges from .xlsx/.xls files with full control over headers, data types, and metadata columns.
- **ReadFlatFile** `01-Data-Connectors/01-Input/02-Structured-Files/flatfile.json` — Creates a dataset with output schema from schema field with values extracted from fixedlength.
- **Read HANA CSV** `01-Data-Connectors/01-Input/02-Structured-Files/hanacsv.json` — It reads in HANA CSV files and creates a DataFrame from it.
- **InMemoryDataset** `01-Data-Connectors/01-Input/02-Structured-Files/inMemoryDataset.json` — In-Memory Dataset Node - Create a DataFrame directly from inline data definitions without reading from external files.
- **Read JSON** `01-Data-Connectors/01-Input/02-Structured-Files/json.json` — Dataset Node for Reading JSON Files.
- **Read LIBSVM** `01-Data-Connectors/01-Input/02-Structured-Files/libsvm.json` — It reads in LIBSVM files and creates a DataFrame from it.
- **Read Parquet** `01-Data-Connectors/01-Input/02-Structured-Files/parquet.json` — Dataset Node for reading Apache Parquet Files.
- **Read Shape File** `01-Data-Connectors/01-Input/02-Structured-Files/shapefile.json` — It reads in Shape files and creates a DataFrame from it.
- **Dataset Structured** `01-Data-Connectors/01-Input/02-Structured-Files/structured.json` — This Node creates a DataFrame by reading data from HDFS, HIVE etc.
- **URL Text File Reader** `01-Data-Connectors/01-Input/02-Structured-Files/urllinereader.json` — Reads a text file from the given URL and creates a DataFrame from it.
- **URL Single Record JSON Reader** `01-Data-Connectors/01-Input/02-Structured-Files/urlsinglerecordjsonreader.json` — It reads single record JSON from the given URL and creates a DataFrame from it.
- **Read XML** `01-Data-Connectors/01-Input/02-Structured-Files/xml.json` — It reads in XML files and creates a DataFrame from it.

## Unstructured Files
- **Binary Files** `01-Data-Connectors/01-Input/03-Unstructured-Files/binaryfiles.json` — Reads in Binary Files from a given path and loads them as FileName/Content.
- **PDF** `01-Data-Connectors/01-Input/03-Unstructured-Files/pdf.json` — Reads in PDF Files from a given path and extracts the text content from them.
- **PDF Image OCR** `01-Data-Connectors/01-Input/03-Unstructured-Files/pdfimageocr.json` — Reads in PDF Files from a given path, extracts the images from them, and converts them to text with Tesseract.
- **Text Files** `01-Data-Connectors/01-Input/03-Unstructured-Files/textfiles.json` — Reads Text Files from a given path and loads each line as a separate row.
- **Tika** `01-Data-Connectors/01-Input/03-Unstructured-Files/tika.json` — Reads in files from a given path and parses them with Apache Tika.
- **Whole Text Files** `01-Data-Connectors/01-Input/03-Unstructured-Files/wholetextfiles.json` — Reads Whole Text Files directory from a given path and loads each file as a separate Row with key (file name) and values (file content).

## SFTP
- **SFTP Read** `01-Data-Connectors/01-Input/05-SFTP/read_sftp.json` — This node reads data from SFTP location with format(csv, txt, json, avro and parquet) and return the dataframe.
- **SFTP** `01-Data-Connectors/01-Input/05-SFTP/sftp.json` — SFTP: This node download the file from SFTP location to target location.

## Enterprise Applications
- **Read Shopify** `01-Data-Connectors/01-Input/06-Enterprise-Applications/read-shopify.json` — This node reads data from Shopify.
- **Read Marketo** `01-Data-Connectors/01-Input/06-Enterprise-Applications/readmarketo.json` — This node reads data from Marketo Files.
- **Read Salesforce** `01-Data-Connectors/01-Input/06-Enterprise-Applications/readsalesforce.json` — This node reads data from Salesforce.

## Database
- **Insert Into HIVE Table** `01-Data-Connectors/02-Output/01-Database/insertintotable.json` — Saves the DataFrame into an Apache HIVE Table.
- **Save JDBC** `01-Data-Connectors/02-Output/01-Database/pyspark_save_jdbc.json` — This node writes data to databases using JDBC.
- **Save Cassandra** `01-Data-Connectors/02-Output/01-Database/saveCassandra.json` — Saves the rows of the incoming DataFrame into Apache Cassandra.
- **Save DynamoDB** `01-Data-Connectors/02-Output/01-Database/saveDynamoDB.json` — Saves the rows of the incoming DataFrame into DynamoDB and get the credentials from the instance profile.
- **Save Iceberg** `01-Data-Connectors/02-Output/01-Database/saveIcebergTable.json` — Reads The Dataframe from the previous node and produces The incoming Dataframe is passed to the next node as it is.
- **Write To BigQuery** `01-Data-Connectors/02-Output/01-Database/save_bigquery.json` — Reads The Dataframe from the previous node and produces The incoming Dataframe is passed to the next node as it is.
- **Save Incorta** `01-Data-Connectors/02-Output/01-Database/save_incorta.json` — Executes the Save Incorta operation.
- **Save As HIVE Table** `01-Data-Connectors/02-Output/01-Database/saveashivetable.json` — Saves the DataFrame into an Apache HIVE Table.
- **Save Databricks Table** `01-Data-Connectors/02-Output/01-Database/savedatabrickstable.json` — This node saves the input data as table in Databricks.
- **Save ElasticSearch** `01-Data-Connectors/02-Output/01-Database/saveelasticsearch.json` — Stores the rows of the incoming DataFrame into Elastic Search.
- **Save MongoDB** `01-Data-Connectors/02-Output/01-Database/savemongodb.json` — It Saves the incoming Dataframe into MongoDB.
- **Update JDBC** `01-Data-Connectors/02-Output/01-Database/update.json` — This node update the data to selected columns.
- **Upsert JDBC** `01-Data-Connectors/02-Output/01-Database/upsertjdbc.json` — This node insert or update the data to databases using JDBC.
- **Write To Snowflake** `01-Data-Connectors/02-Output/01-Database/writeToSnowFlake.json` — Reads The Dataframe from the previous node and produces The incoming Dataframe is passed to the next node as it is.

## Structured Files
- **Save DOCX** `01-Data-Connectors/02-Output/02-Structured-Files/save_docx.json` — Saves DataFrame responses as DOCX files.
- **Save Excel** `01-Data-Connectors/02-Output/02-Structured-Files/save_excel.json` — Saves the DataFrame into the specified location in XLS Format.
- **Save Excel Advanced** `01-Data-Connectors/02-Output/02-Structured-Files/save_excel_advanced.json` — Powerful Excel Writer Node – Export DataFrames to .xlsx files with full control over sheets, ranges, dynamic naming, record splitting, formatting preservation, password protection, and advanced save modes.
- **Save HTML** `01-Data-Connectors/02-Output/02-Structured-Files/save_html.json` — Saves DataFrame responses as HTML files.
- **Save PDF** `01-Data-Connectors/02-Output/02-Structured-Files/save_pdf.json` — Saves DataFrame responses as PDF files.
- **Save Text** `01-Data-Connectors/02-Output/02-Structured-Files/save_textfile.json` — Saves the DataFrame into the specified location in Text Format.
- **Save Avro** `01-Data-Connectors/02-Output/02-Structured-Files/saveavro.json` — Saves the DataFrame into the specified location in Apache Avro Format.
- **Save CSV** `01-Data-Connectors/02-Output/02-Structured-Files/savecsv.json` — Saves the DataFrame into the specified location in CSV Format.
- **Save Delta** `01-Data-Connectors/02-Output/02-Structured-Files/savedelta.json` — Saves the DataFrame into the specified location in Delta Format.
- **Save JDBC** `01-Data-Connectors/02-Output/02-Structured-Files/savejdbc.json` — This node writes data to databases using JDBC.
- **Save JSON** `01-Data-Connectors/02-Output/02-Structured-Files/savejson.json` — Saves the DataFrame into the specified location in JSON Format.
- **Save ORC** `01-Data-Connectors/02-Output/02-Structured-Files/saveorc.json` — Saves the DataFrame into the specified location in ORC Format.
- **Save Parquet** `01-Data-Connectors/02-Output/02-Structured-Files/saveparquet.json` — Saves the DataFrame into the specified location in Parquet Format.

## Streaming
- **Kafka Producer** `01-Data-Connectors/02-Output/04-Streaming/kafkaproducer.json` — Write out the Dataframe to a specified Apache Kafka Topic.

## SFTP
- **SFTP Write** `01-Data-Connectors/02-Output/05-SFTP/write_sftp.json` — This node save the data to sftp location with given format like csv, txt, json, avro and parquet.

## Enterprise Applications
- **Save Shopify Resource** `01-Data-Connectors/02-Output/06-Enterprise-Applications/save-shopify.json` — This node saves data to Shopify.

## Real Time Streaming
- **Streaming Kafka** `01-Data-Connectors/03-Streaming/01-Real-Time-Streaming/kafkastreaming.json` — Reads in streaming text from topics in Apache Kafka.
- **Streaming Socket Text Stream** `01-Data-Connectors/03-Streaming/01-Real-Time-Streaming/socketstreaming.json` — Reads in streaming text from a socket.
- **Streaming Text File Stream** `01-Data-Connectors/03-Streaming/01-Real-Time-Streaming/textfilestreaming.json` — It monitors a specified directory for new files.

## Structured Streaming
- **Structured Streaming Console Sink** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/consolestructuredstreaming.json` — It outputs the DataFrame to the console.
- **Structured Streaming CSV** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/csvstructuredstreaming.json` — It monitors a specified directory for new files.
- **Structured Streaming File Sink** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/filesinkstructuredstreaming.json` — It writes the DataFrame to files with Structured Streaming.
- **Structured Streaming JSON** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/jsonstructuredstreaming.json` — It monitors a specified directory for new files.
- **Structured Streaming Kafka Read** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/kafkastructuredstreaming.json` — Reads in streaming text from topics in Apache Kafka.
- **Structured Streaming Kafka Save** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/kafkastructuredstreamingsave.json` — Reads in streaming text from topics in Apache Kafka.
- **Structured Streaming Kinesis** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/kinesisstructuredstreaming.json` — Reads in streaming text from Kinesis stream.
- **Structured Streaming Socket** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/socketstructuredstreaming.json` — Reads in streaming text from a socket.
- **Structured Streaming Hive Sink** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/structuredstreamingfilesink.json` — Saves the streaming data into a HIVE Table.
- **Structured Streaming Hive Sink2** `01-Data-Connectors/03-Streaming/02-Structured-Streaming/structuredstreaminghivesink2.json` — Saves the streaming data into an Apache HIVE Table.

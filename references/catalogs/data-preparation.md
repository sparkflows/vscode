# Data Preparation Nodes

## DateTime
- **Date Time Field Extract** `03-Data-Preparation/01-DateTime/datetimefieldextract.json` — It creates a new DataFrame by extracting Date and Time fields.
- **Date To Age** `03-Data-Preparation/01-DateTime/datetoage.json` — This node converts a date-column into columns of age (both in years and in days).
- **Date Difference** `03-Data-Preparation/01-DateTime/datetodiff.json` — This node finds difference between two dates.
- **Date To String** `03-Data-Preparation/01-DateTime/datetostring.json` — This node converts a date/time column to string with given format.
- **String To Date** `03-Data-Preparation/01-DateTime/stringtodatemulti.json` — This node converts string columns to date using the specified date/time format.
- **String To Unix Time** `03-Data-Preparation/01-DateTime/stringtounixtime.json` — This node converts a string to Unix Time.
- **Time Functions** `03-Data-Preparation/01-DateTime/timeFunctions.json` — This node extracts year, dayofmonth, dayofyear, weekofyear, dayofweek, quarter, hour, minute, second & season.
- **Unix Time To String** `03-Data-Preparation/01-DateTime/unixtimetostring.json` — This node converts Unix Time to String.

## Math
- **Math Expression** `03-Data-Preparation/02-Math/mathexpression.json` — Creates new columns using the specified expressions.
- **Math Functions** `03-Data-Preparation/02-Math/mathfunctionsmultiple.json` — Create new columns or replaces the existing ones by using the specified function.

## String
- **String Functions** `03-Data-Preparation/03-String/stringfunctionsmultiple.json` — String Functions Multiple.
- **Text Case Transformer** `03-Data-Preparation/03-String/textCaseTransformer.json` — This node converts the text of the selected column to upper or lower case.

## Parsing
- **Apache Logs** `03-Data-Preparation/04-Parsing/apachelogs.json` — Reads in Apache Log files from a given path, parses them and loads them into a DataFrame.
- **Field Splitter** `03-Data-Preparation/04-Parsing/fieldsplitter.json` — This node splits the string of the specified input column using the specified delimiter.
- **Fixed Length Fields** `03-Data-Preparation/04-Parsing/fixedlength.json` — Reads in files with fixed length fields.
- **Multi Regex Extractor** `03-Data-Preparation/04-Parsing/multiregexextractor.json` — This node is used to extract pattern from input columns.
- **OCR** `03-Data-Preparation/04-Parsing/ocrtesseract.json` — Performs Optical Character Recognition using the Tesseract Library.
- **Paragraph Splitter** `03-Data-Preparation/04-Parsing/paragraphsplitter.json` — Executes the Paragraph Splitter operation.
- **Parse JSON Col** `03-Data-Preparation/04-Parsing/parsejsoncol.json` — Parses JSON content in a given column.
- **Parse XML Col** `03-Data-Preparation/04-Parsing/parsexmlcol.json` — Parses XML content in a given column.
- **Regex Tokenizer** `03-Data-Preparation/04-Parsing/regextokenizer.json` — This node creates a new DataFrame by the process of taking text (such as a sentence) and breaking it into individual terms (usually words) based on regular expression.
- **Text To Columns** `03-Data-Preparation/04-Parsing/texttocolumns.json` — Use Text To Columns to take the text in one column and split the string value into separate, multiple columns (or rows), based on a single or multiple delimiters.

## Cleaning
- **Imputing With Constant** `03-Data-Preparation/05-Cleaning/ImputingWithConstant.json` — It imputes missing value with constant value.
- **Imputing With Mean Value** `03-Data-Preparation/05-Cleaning/ImputingWithMeanValue.json` — Imputing the continuous variables by mean.
- **Imputing With Median** `03-Data-Preparation/05-Cleaning/ImputingWithMedianValue.json` — Imputing with median.
- **Imputing With Mode Value** `03-Data-Preparation/05-Cleaning/ImputingWithModeValue.json` — Imputing with most frequently observed value.
- **Count rows columns** `03-Data-Preparation/05-Cleaning/count_rows_columns_python.json` — Executes the Count rows columns operation.
- **Data Cleansing** `03-Data-Preparation/05-Cleaning/data_cleansing.json` — One-stop data quality powerhouse – instantly clean dozens of common messy data issues: null handling, whitespace, unwanted characters, case standardization, and more.
- **Data Cleansing Advanced** `03-Data-Preparation/05-Cleaning/data_cleansing_advanced.json` — This node cleanses the selected columns from the dataset.
- **Data Wrangling** `03-Data-Preparation/05-Cleaning/datawrangling.json` — This node creates a new DataFrame by applying each of the Rules specified.
- **Dedup** `03-Data-Preparation/05-Cleaning/dedup.json` — This node is used for problems like entity resolution or data matching.
- **Drop Duplicate Rows** `03-Data-Preparation/05-Cleaning/dropduplicaterows.json` — Drops duplicate rows from the incoming DataFrame.
- **Drop Rows With Null** `03-Data-Preparation/05-Cleaning/droprowswithnull.json` — This node creates a new DataFrame by dropping rows containing null values.
- **Drop Null Rows for Selected Columns** `03-Data-Preparation/05-Cleaning/droprowswithnull_multiple_cols.json` — This node creates a new DataFrame by dropping rows containing null values for selected Columns.
- **Find And Replace Using Regex** `03-Data-Preparation/05-Cleaning/findAndReplaceusingregex.json` — This node finds and replaces text in a column with another.
- **Find And Replace Using Regex Advanced** `03-Data-Preparation/05-Cleaning/findandreplaceusingregexmultiple.json` — This node finds and replaces text in a column containing string.
- **Impute Advanced** `03-Data-Preparation/05-Cleaning/impute.json` — Advanced Imputation Node - Handle missing or specified values in numeric columns using statistical strategies such as mean, median, mode, or a user-defined constant.
- **Lookup** `03-Data-Preparation/05-Cleaning/nodelookup.json` — Find values in a target column using a lookup table and either append fields or replace matched text.
- **Count Null Values** `03-Data-Preparation/05-Cleaning/null_count_python.json` — Counts null value in columns using the specified input.
- **Remove Unwanted Characters** `03-Data-Preparation/05-Cleaning/removeUnwantedCharacters.json` — This node removes unwanted characters from the specified input columns.
- **Remove Duplicate Rows** `03-Data-Preparation/05-Cleaning/removeduplicaterows.json` — This node take an array of fields and compare the rows on those fields.
- **Remove Unwanted Characters Advanced** `03-Data-Preparation/05-Cleaning/removeunwantedcharactersmultiple.json` — This node removes unwanted characters.
- **Standard Deviation** `03-Data-Preparation/05-Cleaning/standarddeviation_python.json` — Creates new columns using the specified input columns.
- **Value count** `03-Data-Preparation/05-Cleaning/value_count_python.json` — Counts value in columns using the specified input.

## Add Column
- **Add  Columns** `03-Data-Preparation/06-Add-Column/addcolumns.json` — This node allows adding new columns with certain values.
- **Add Column Advanced** `03-Data-Preparation/06-Add-Column/addconstantcolumns.json` — This node allows adding new columns with certain values.
- **BulkColumnExpression** `03-Data-Preparation/06-Add-Column/bulkcolumnexpressions.json` — Bulk Column Expression Node - Create or update multiple columns at once using a single Spark SQL expression.
- **Case When** `03-Data-Preparation/06-Add-Column/casewhen.json` — This node creates a new Dataframe with a new column appended to it containing value based on the condition met.
- **Case When Advanced** `03-Data-Preparation/06-Add-Column/casewhenmultiple.json` — This node creates a new Dataframe with a new column appended to it containing value based on the condition met.
- **Concat Columns** `03-Data-Preparation/06-Add-Column/concatcolumns.json` — This node creates a new DataFrame by concatenating the specified columns of the input DataFrame.
- **Expressions** `03-Data-Preparation/06-Add-Column/expressions.json` — The most powerful and intuitive column calculator - add unlimited new columns using full Spark SQL expressions.
- **Record ID** `03-Data-Preparation/06-Add-Column/generateRecordID.json` — Adds a sequential Record ID column to the dataset, similar to Alteryx Record ID Tool.
- **Generate UUID** `03-Data-Preparation/06-Add-Column/generateUUID.json` — This node Generates a Universally Unique ID.
- **Generate Rows** `03-Data-Preparation/06-Add-Column/generaterows.json` — Creates new rows of data at the record level using iterative expressions.
- **Generate UID** `03-Data-Preparation/06-Add-Column/generateuid.json` — This node Generates a new column with unique Index/Value for each row in the Dataset for each partition.
- **Data Masking** `03-Data-Preparation/06-Add-Column/hash.json` — This node adds a new column which contains the Hash of the specified columns.
- **Row Numbering** `03-Data-Preparation/06-Add-Column/rownumbering.json` — Executes the Row Numbering operation.
- **Zip With Index** `03-Data-Preparation/06-Add-Column/zipwithindex.json` — This node Generates a new column with unique Index/Value for each row in the Dataset.

## Control Structures
- **Execute In Loop** `03-Data-Preparation/06-Control-Structures/executeinloop.json` — Executes the Execute In Loop operation.
- **Execute Workflow** `03-Data-Preparation/06-Control-Structures/executeworkflow.json` — Fires the given workflow.
- **Read Parameters** `03-Data-Preparation/06-Control-Structures/readparameters.json` — Reads in the parameters from the given file.
- **Specify Parameters** `03-Data-Preparation/06-Control-Structures/specifyparameters.json` — Provides additional parameters to the workflow.

## Split
- **Compare All Columns** `03-Data-Preparation/07-Split/compare.json` — Compares 2 incoming DataFrames.
- **Compare All Columns Single Output** `03-Data-Preparation/07-Split/compareallcolumnssingleoutput.json` — Compares 2 incoming DataFrames.
- **Compare Specific Columns** `03-Data-Preparation/07-Split/comparespecificcolumns.json` — Compares 2 incoming DataFrames on specific columns.
- **Compare Specific Columns Single Output** `03-Data-Preparation/07-Split/comparespecificcolumnssingleoutput.json` — Compares 2 incoming DataFrames on specific columns.
- **Split By Expression** `03-Data-Preparation/07-Split/splitbyexpression.json` — This node splits the incoming DataFrame into two output DataFrames by applying the conditional logic.
- **Split By Multiple Expressions** `03-Data-Preparation/07-Split/splitbymultipleexpressions.json` — Splits the incoming DataFrame into multiple output DataFrames by applying the conditional logic.

## Condition
- **Assert** `03-Data-Preparation/08-Condition/assert.json` — This Node takes in an expression.
- **Decision** `03-Data-Preparation/08-Condition/decision.json` — It computes expressions to determine if the condition is met or not.

## Cast DataType
- **Cast To Single Type** `03-Data-Preparation/09-Cast-DataType/castcolumntype.json` — This node creates a new DataFrame by casting the specified input columns to a new data type.
- **Cast To Different Types-1** `03-Data-Preparation/09-Cast-DataType/castcolumntypemulti.json` — This node creates a new DataFrame by casting the specified columns into new types.
- **Cast To Different Types-2** `03-Data-Preparation/09-Cast-DataType/castcolumntypemulti2.json` — This node creates a new DataFrame by casting the specified columns into new types.

## Filter
- **Select Columns** `03-Data-Preparation/10-Filter/columnfilter.json` — This node creates a new DataFrame that contains only the selected columns.
- **Drop Columns** `03-Data-Preparation/10-Filter/dropcolumns.json` — This node creates a new DataFrame by dropping the specified columns.
- **Dynamic Select** `03-Data-Preparation/10-Filter/dynamic_select.json` — Dynamically select or de-select columns using Spark expressions or column metadata.
- **Filter Advanced** `03-Data-Preparation/10-Filter/filterAdvanced.json` — Advanced Filter Node - Split incoming data into two logical outputs based on flexible conditions.
- **Filter By Date Range** `03-Data-Preparation/10-Filter/filterByDateRange.json` — This node filters Rows within the given date range.
- **Filter By String Length** `03-Data-Preparation/10-Filter/filterByStringLength.json` — This node filters the Rows within the given string length.
- **Limit** `03-Data-Preparation/10-Filter/limit.json` — This node Limits the number of rows in the output.
- **Filter By Number Range** `03-Data-Preparation/10-Filter/numberRangeFilter.json` — This node filters the rows in the given Number Range.
- **Regex Advanced** `03-Data-Preparation/10-Filter/regex.json` — Advanced Regex Node - Perform powerful regular expression-based text processing including parsing, tokenization, replacement, and pattern matching.
- **Node Row Filter By Index** `03-Data-Preparation/10-Filter/rowFilterWithIndex.json` — This node creates a new DataFrame containing only rows satisfying given condition.
- **Row Filter** `03-Data-Preparation/10-Filter/rowfilter.json` — This node creates a new DataFrame containing the rows that satisfy the given condition.
- **Select** `03-Data-Preparation/10-Filter/select.json` — The ultimate column selector - pick, rename, cast, drop, and propagate columns with pixel-perfect control.
- **FindDuplicate** `03-Data-Preparation/10-Filter/unique.json` — This node splits the incoming DataFrame into two output DataFrames one having unique values and other having rest of duplicates.

## Join Union
- **Append Fields** `03-Data-Preparation/11-Join-Union/appendfields.json` — Append fields from a Source DataFrame to every row of a Target DataFrame (Cartesian-style append).
- **Join On Columns** `03-Data-Preparation/11-Join-Union/joinoncolumns.json` — Joins the incoming Dataframes on the given columns.
- **Join On Common Column** `03-Data-Preparation/11-Join-Union/joinoncommoncolumn.json` — This node joins the incoming dataframes using one common column between them.
- **Join On Common Columns** `03-Data-Preparation/11-Join-Union/joinoncommoncolumns.json` — This node joins the incoming dataframes on 1 or more columns.
- **Join Using SQL** `03-Data-Preparation/11-Join-Union/joinusingsql.json` — This node registers the incoming DataFrames as temporary tables and executes the SQL provided.
- **Join Advanced** `03-Data-Preparation/11-Join-Union/nodejoin.json` — Advanced Join Node - Combine two DataFrames using flexible join strategies with full control over join keys, column selection, renaming, data types, and schema propagation.
- **Union Advanced** `03-Data-Preparation/11-Join-Union/unionadvanced.json` — Smart Union node that combines multiple DataFrames with full control: union by column name or position, include all columns or only common ones, and automatically handle mismatched schemas with null padding.
- **Union All** `03-Data-Preparation/11-Join-Union/unionall.json` — This node creates a new DataFrame by doing a union of all the rows in the incoming Dataframes.
- **Union Distinct** `03-Data-Preparation/11-Join-Union/uniondistinct.json` — This node creates a new DataFrame by performing a UNION of all the rows in the incoming Dataframe.

## Group
- **Aggregate** `03-Data-Preparation/12-Group/aggregate.json` — The most powerful and flexible aggregation node - combines Group By, multiple aggregations, Pivot, conditional expressions, and column propagation in one easy-to-use interface.
- **Cube** `03-Data-Preparation/12-Group/cube.json` — Cube Node generates a result set that shows aggregates for all combinations of values in the selected columns.
- **Group By** `03-Data-Preparation/12-Group/grouper.json` — Group By Node.
- **Melt** `03-Data-Preparation/12-Group/melt_python.json` — Melt Node.
- **Pivot By** `03-Data-Preparation/12-Group/pivot.json` — Pivot Node.
- **Pivot By Advanced** `03-Data-Preparation/12-Group/pivot_advance.json` — Pivot Node with advanced options.
- **Pivot By** `03-Data-Preparation/12-Group/pivot_python.json` — Pivot Node.
- **Rollup** `03-Data-Preparation/12-Group/rollup.json` — Rollup Node generates a result set that shows aggregates for a hierarchy of values in the selected columns.

## Code
- **SQL Executer** `03-Data-Preparation/13-Code/SQLExecuter.json` — This node runs the given SQL query.
- **Scala** `03-Data-Preparation/13-Code/databricks_scala.json` — This node runs any given Scala code.
- **Jython** `03-Data-Preparation/13-Code/jython.json` — This node runs any given Jython code.
- **MultiInputPySpark** `03-Data-Preparation/13-Code/multi_input_pyspark.json` — This node runs any given PySpark code.
- **Multi Input To Multi Output PySpark** `03-Data-Preparation/13-Code/multiinput_to_multioutput_pyspark.json` — This node runs any given PySpark code.
- **Polars** `03-Data-Preparation/13-Code/polars.json` — This node runs any given Polars code.
- **PySpark** `03-Data-Preparation/13-Code/pyspark.json` — This node runs any given PySpark code.
- **Run Python Code** `03-Data-Preparation/13-Code/run_python_code.json` — This node executes the given python code.
- **Run Python File** `03-Data-Preparation/13-Code/run_python_file.json` — This node executes the given python file.
- **Run HIVEQL** `03-Data-Preparation/13-Code/runhivehql.json` — This node runs the given SQL on the incoming DataFrame.
- **Spark** `03-Data-Preparation/13-Code/scala.json` — This node runs any given Scala code.
- **Scala UDF** `03-Data-Preparation/13-Code/scalaudf.json` — This node runs any given Scala code for UDFs.
- **SQL** `03-Data-Preparation/13-Code/sql.json` — This node runs the given SQL on the incoming DataFrame.
- **Unix Shell Commands** `03-Data-Preparation/13-Code/unixShellCommand.json` — This node executes shell command.

## Others
- **CDC Using Full Table Merge** `03-Data-Preparation/16-Others/cdcusingfulltablemerge.json` — CDC Using Full Table Merge.
- **Columns Rename** `03-Data-Preparation/16-Others/columnsrename.json` — This node creates a new DataFrame by renaming existing columns with the new name.
- **Compare Columns** `03-Data-Preparation/16-Others/compare_columns.json` — Compare columns between two DataFrames using key ID columns.
- **Count** `03-Data-Preparation/16-Others/count.json` — This node counts the number of records in the incoming Dataframe and puts the count into result page.
- **CountRecords** `03-Data-Preparation/16-Others/countrecords.json` — This node counts the number of rows in a dataset in different ways.
- **Dynamic Rename** `03-Data-Preparation/16-Others/dynamicrename.json` — This node creates a new DataFrame by renaming existing columns with the new name.
- **Explode** `03-Data-Preparation/16-Others/explode.json` — Explode the array of values into multiple rows with columnname_explode.
- **Flatten** `03-Data-Preparation/16-Others/flatten.json` — Processes Flatten the nested structure in struct into given column.
- **Formula** `03-Data-Preparation/16-Others/formula.json` — test.
- **JsonToEDI** `03-Data-Preparation/16-Others/jsontoedi.json` — Executes the JsonToEDI operation.
- **Linear Programming Optimisation** `03-Data-Preparation/16-Others/lpo.json` — Executes the Linear Programming Optimisation operation.
- **Multi Window Analytics** `03-Data-Preparation/16-Others/multiwindowanalyticsfunctions.json` — Executes the Multi Window Analytics operation.
- **Multi Window Ranking** `03-Data-Preparation/16-Others/multiwindowrankingfunctions.json` — Executes the Multi Window Ranking operation.
- **DeltaMerge** `03-Data-Preparation/16-Others/nodedeltacdc.json` — Insert, delete and update data using the Delta merge command.
- **Recover Hive Partitions** `03-Data-Preparation/16-Others/recoverhivepartitions.json` — Node to recover the partitions of external hive table.
- **Register TempTable** `03-Data-Preparation/16-Others/registerteamptable.json` — This node registers the incoming DataFrame as a temporary table in Spark.
- **Round Value** `03-Data-Preparation/16-Others/rounddouble.json` — Processes It takes in a DataFrame as input data.
- **Sample** `03-Data-Preparation/16-Others/sample.json` — Samples the incoming DataFrame.
- **SaveWaterMark** `03-Data-Preparation/16-Others/savewatermark.json` — This node saves the value in watermark variable in workflow to file.
- **SCDType2DeltaMerge** `03-Data-Preparation/16-Others/scdtype2deltamerge.json` — It is a Delta merge operation that stores and manages both current and historical data over time.
- ** Scheduling Optimization** `03-Data-Preparation/16-Others/scheduling_optimisation.json` — Node to optimize production scheduling in manufacturing environments by incorporating preventive maintenance and handling operational uncertainties.
- **Sort By** `03-Data-Preparation/16-Others/sortby.json` — Sorts the entire DataFrame by one or multiple columns with full control over ascending/descending order per column.
- **Sort Columns** `03-Data-Preparation/16-Others/sortcolumns.json` — It sorts the columns selection.
- ** Supplier Optimization** `03-Data-Preparation/16-Others/supplier_optimisation.json` — Executes the  Supplier Optimization operation.
- **Transpose** `03-Data-Preparation/16-Others/transpose.json` — This node transposes a dataframe without performing aggregation function by given column(transposeby).
- **Unpivot** `03-Data-Preparation/16-Others/transpose_columns.json` — Transpose Node.
- **Window Aggregation** `03-Data-Preparation/16-Others/windowaggregation.json` — This node calculates the moving values of selected functions for the field(input column).
- **Window Analytics** `03-Data-Preparation/16-Others/windowanalytics.json` — Executes the Window Analytics operation.
- **Window Function** `03-Data-Preparation/16-Others/windowfunction.json` — This node applies window functions to the input DataFrame, allowing operations like ranking, analytical, and aggregate functions over specified windows.
- **Window Ranking** `03-Data-Preparation/16-Others/windowranking.json` — Executes the Window Ranking operation.
- **Word Count** `03-Data-Preparation/16-Others/wordcount.json` — Executes the Word Count operation.

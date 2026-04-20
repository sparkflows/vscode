# Data Quality Nodes

## General
- **NodeDataQualityCheckAndAlert** `06-Data-Quality/NodeDataQualityCheckAndAlert.json` — This node is used to perform data quality checks on a DataFrame and send alerts based on the results.
- **HasDataSize** `06-Data-Quality/checkHasDataSize.json` — Check the size of the dataset.
- **HasMax** `06-Data-Quality/checkHasMax.json` — Check for max value in selected column.
- **HasMin** `06-Data-Quality/checkHasMin.json` — Check for min value in selected column.
- **IsExpression** `06-Data-Quality/checkIsExpression.json` — Evaluate one or more boolean expressions on the DataFrame rows.
- **PatternMatch** `06-Data-Quality/checkPattern.json` — Executes the PatternMatch operation.
- **IsNonNegative** `06-Data-Quality/isNonNegative.json` — Should not contain negative values.
- **Is Not Null** `06-Data-Quality/isNotNull.json` — Executes the Is Not Null operation.
- **IsPositive** `06-Data-Quality/isPositive.json` — Executes the IsPositive operation.
- **Is Primary Key** `06-Data-Quality/isPrimaryKey.json` — Executes the Is Primary Key operation.
- **Is Value In** `06-Data-Quality/isValueIn.json` — Executes the Is Value In operation.
- **CheckOutliers** `06-Data-Quality/outlier.json` — This checks if values fall between Inter Quartile Range.
- **ColumnValuesToBeBetween** `06-Data-Quality/range.json` — Executes the ColumnValuesToBeBetween operation.

## Great Expectations
- **Create CSV from GE Results** `06-Data-Quality/01-Great-Expectations/create_csv_from_ge_results.json` — Executes the Create CSV from GE Results operation.
- **ExpectColumnToExist** `06-Data-Quality/01-Great-Expectations/expect_column_to_exist.json` — Executes the ExpectColumnToExist operation.
- **ExpectColumnValueLengthToBeInBetween** `06-Data-Quality/01-Great-Expectations/expect_column_value_length_to_be_in_between.json` — Executes the ExpectColumnValueLengthToBeInBetween operation.
- **ExpectColumnValueLengthsToEqual** `06-Data-Quality/01-Great-Expectations/expect_column_value_lengths_to_equal.json` — Executes the ExpectColumnValueLengthsToEqual operation.
- **ExpectColumnValueToMatchStrftimeFormat** `06-Data-Quality/01-Great-Expectations/expect_column_value_to_match_strftime_format.json` — Executes the ExpectColumnValueToMatchStrftimeFormat operation.
- **ExpectColumnValuesToBeInBetween** `06-Data-Quality/01-Great-Expectations/expect_column_values_to_be_in_between.json` — Executes the ExpectColumnValuesToBeInBetween operation.
- **ExpectColumnValuesToBeInSet** `06-Data-Quality/01-Great-Expectations/expect_column_values_to_be_in_set.json` — Executes the ExpectColumnValuesToBeInSet operation.
- **ExpectColumnValuesToBeNull** `06-Data-Quality/01-Great-Expectations/expect_column_values_to_be_null.json` — Executes the ExpectColumnValuesToBeNull operation.
- **ExpectColumnValuesToBeUnique** `06-Data-Quality/01-Great-Expectations/expect_column_values_to_be_unique.json` — Executes the ExpectColumnValuesToBeUnique operation.
- **ExpectColumnValuesToMatchRegex** `06-Data-Quality/01-Great-Expectations/expect_column_values_to_match_regex.json` — Executes the ExpectColumnValuesToMatchRegex operation.
- **ExpectColumnValuesToNotBeNull** `06-Data-Quality/01-Great-Expectations/expect_column_values_to_not_be_null.json` — Executes the ExpectColumnValuesToNotBeNull operation.
- **ExpectTableRowCountToBeBetween** `06-Data-Quality/01-Great-Expectations/expect_table_row_count_to_be_between.json` — Executes the ExpectTableRowCountToBeBetween operation.
- **GE Decision** `06-Data-Quality/01-Great-Expectations/ge_decision.json` — This Node takes in an expression.
- **Split Into Good And Bad Records** `06-Data-Quality/01-Great-Expectations/split_into_good_and_bad_records.json` — Executes the Split Into Good And Bad Records operation.

# 79 SQL Operators

## Overview

SQL operators enable database interactions including queries, DDL, and data manipulation from Airflow workflows. This section covers SQLExecuteQueryOperator, database-specific operators, parameterized queries, result handling, and SQL best practices for Airflow 3.x.

## Research & Background

### Key Concepts
- **SQLExecuteQueryOperator**: Generic SQL execution operator
- **Database Hooks**: Connection management for databases
- **Parameterized Queries**: Safe parameter passing
- **Result Handling**: Process query results
- **Transaction Management**: Commit and rollback

### Airflow 3.x Features
- Unified SQLExecuteQueryOperator
- Improved result handling
- Better parameter binding
- Enhanced connection pooling
- Common SQL interface

### Prerequisites
- Airflow 3.x with database providers
- Database connection configured
- Basic SQL knowledge

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Execute SQL queries from Airflow tasks
2. Handle parameters securely
3. Process query results
4. Manage transactions properly
5. Build efficient SQL workflows

---

# 79.1 SQL Execution Basics

## Overview
Fundamental SQL execution patterns.

## Tasks

### - [ ] 79.1.1 SQLExecuteQueryOperator Introduction
Filename: `79_01_01_sql_execute_query.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Basic SQL execution

- [ ] Import SQLExecuteQueryOperator
- [ ] conn_id for database connection
- [ ] sql parameter with query
- [ ] Single query execution

**Expected Behavior**: Query executes successfully

---

### - [ ] 79.1.2 Multiple SQL Statements
Filename: `79_01_02_multiple_statements.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Execute multiple queries

- [ ] List of SQL statements
- [ ] SQL file execution
- [ ] Statement order
- [ ] Split statements option

**Expected Behavior**: All statements execute

---

### - [ ] 79.1.3 SQL from External Files
Filename: `79_01_03_sql_from_files.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Read SQL from files

- [ ] sql parameter with file path
- [ ] .sql file organization
- [ ] Template rendering in files
- [ ] SQL file best practices

**Expected Behavior**: SQL file executed

---

### - [ ] 79.1.4 Database Connection Types
Filename: `79_01_04_connection_types.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Connect to various databases

- [ ] PostgreSQL connection
- [ ] MySQL connection
- [ ] SQLite connection
- [ ] Connection string formats

**Expected Behavior**: Various databases accessible

---

### - [ ] 79.1.5 Autocommit and Transactions
Filename: `79_01_05_autocommit_transactions.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Control transaction behavior

- [ ] autocommit parameter
- [ ] Explicit transactions
- [ ] Rollback on error
- [ ] Transaction boundaries

**Expected Behavior**: Transaction control works

---

# 79.2 Parameterized Queries

## Overview
Safely passing parameters to SQL queries.

## Tasks

### - [ ] 79.2.1 Parameters Dict
Filename: `79_02_01_parameters_dict.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Pass parameters to queries

- [ ] parameters parameter
- [ ] Named parameters (:name)
- [ ] Positional parameters (%s)
- [ ] Parameter type handling

**Expected Behavior**: Parameters bound safely

---

### - [ ] 79.2.2 Templated Parameters
Filename: `79_02_02_templated_parameters.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use Jinja in parameters

- [ ] Template parameters at render time
- [ ] Access Airflow context
- [ ] Dynamic parameter values
- [ ] XCom in parameters

**Expected Behavior**: Dynamic parameters work

---

### - [ ] 79.2.3 SQL Injection Prevention
Filename: `79_02_03_sql_injection_prevention.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Secure query construction

- [ ] Never concatenate user input
- [ ] Use parameterized queries
- [ ] Validate identifiers
- [ ] Audit query patterns

**Expected Behavior**: Queries secure from injection

---

### - [ ] 79.2.4 Bulk Parameters
Filename: `79_02_04_bulk_parameters.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Execute with multiple param sets

- [ ] List of parameter dicts
- [ ] Bulk insert patterns
- [ ] executemany behavior
- [ ] Performance optimization

**Expected Behavior**: Bulk operations efficient

---

### - [ ] 79.2.5 Dynamic SQL Generation
Filename: `79_02_05_dynamic_sql.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Build SQL dynamically

- [ ] Conditional query parts
- [ ] Table/column selection
- [ ] Safe identifier quoting
- [ ] Query builder patterns

**Expected Behavior**: Dynamic SQL generated safely

---

# 79.3 Result Handling

## Overview
Processing SQL query results.

## Tasks

### - [ ] 79.3.1 Return Results to XCom
Filename: `79_03_01_results_to_xcom.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Store query results

- [ ] return_last=True
- [ ] do_xcom_push=True
- [ ] Result format
- [ ] XCom size limits

**Expected Behavior**: Results in XCom

---

### - [ ] 79.3.2 Handler Functions
Filename: `79_03_02_handler_functions.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Process results with function

- [ ] handler parameter
- [ ] Transform result rows
- [ ] Aggregate results
- [ ] Custom output format

**Expected Behavior**: Handler processes results

---

### - [ ] 79.3.3 Fetch Modes
Filename: `79_03_03_fetch_modes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Control result fetching

- [ ] fetch_all vs fetch_one
- [ ] Large result handling
- [ ] Cursor iteration
- [ ] Memory management

**Expected Behavior**: Appropriate fetch mode used

---

### - [ ] 79.3.4 Result Row Processing
Filename: `79_03_04_row_processing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Process rows downstream

- [ ] Access results in tasks
- [ ] Row-by-row processing
- [ ] Map over results
- [ ] Error handling per row

**Expected Behavior**: Rows processed correctly

---

### - [ ] 79.3.5 Large Result Sets
Filename: `79_03_05_large_results.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle large query results

- [ ] Chunked fetching
- [ ] Streaming results
- [ ] Write to file
- [ ] Avoid memory issues

**Expected Behavior**: Large results handled

---

# 79.4 Database-Specific Patterns

## Overview
Patterns for specific databases.

## Tasks

### - [ ] 79.4.1 PostgreSQL Patterns
Filename: `79_04_01_postgresql_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: PostgreSQL-specific features

- [ ] PostgresOperator
- [ ] COPY command
- [ ] Array and JSON types
- [ ] PL/pgSQL execution

**Expected Behavior**: PostgreSQL features work

---

### - [ ] 79.4.2 MySQL Patterns
Filename: `79_04_02_mysql_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: MySQL-specific features

- [ ] MySqlOperator
- [ ] LOAD DATA INFILE
- [ ] Stored procedures
- [ ] Multi-statement execution

**Expected Behavior**: MySQL features work

---

### - [ ] 79.4.3 BigQuery Patterns
Filename: `79_04_03_bigquery_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: BigQuery SQL execution

- [ ] BigQueryInsertJobOperator
- [ ] Standard SQL mode
- [ ] Query parameters
- [ ] Cost control

**Expected Behavior**: BigQuery queries work

---

### - [ ] 79.4.4 Snowflake Patterns
Filename: `79_04_04_snowflake_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Snowflake SQL execution

- [ ] SnowflakeOperator
- [ ] Warehouse selection
- [ ] Multi-statement support
- [ ] Query tags

**Expected Behavior**: Snowflake queries work

---

### - [ ] 79.4.5 SQLite Patterns
Filename: `79_04_05_sqlite_patterns.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`

**Purpose**: SQLite for testing/simple use

- [ ] SqliteOperator
- [ ] File-based database
- [ ] Testing DAGs locally
- [ ] Limitations

**Expected Behavior**: SQLite works for simple cases

---

# 79.5 Advanced SQL Workflows

## Overview
Complex SQL-based workflow patterns.

## Tasks

### - [ ] 79.5.1 SQL Check Operators
Filename: `79_05_01_sql_check_operators.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Data validation with SQL

- [ ] SQLCheckOperator
- [ ] SQLValueCheckOperator
- [ ] SQLIntervalCheckOperator
- [ ] Fail on check failure

**Expected Behavior**: Data validation works

---

### - [ ] 79.5.2 Branch by SQL Result
Filename: `79_05_02_branch_by_sql.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Conditional flow based on query

- [ ] BranchSQLOperator
- [ ] Query returns path
- [ ] Multiple branches
- [ ] Null handling

**Expected Behavior**: Correct branch selected

---

### - [ ] 79.5.3 ETL with SQL Operators
Filename: `79_05_03_etl_sql.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: SQL-based ETL pattern

- [ ] Extract with SELECT
- [ ] Transform with SQL
- [ ] Load with INSERT
- [ ] Incremental loads

**Expected Behavior**: ETL pipeline works

---

### - [ ] 79.5.4 Stored Procedure Execution
Filename: `79_05_04_stored_procedures.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Call stored procedures

- [ ] CALL/EXEC syntax
- [ ] Input parameters
- [ ] Output parameters
- [ ] Return values

**Expected Behavior**: Procedures execute

---

### - [ ] 79.5.5 Cross-Database Queries
Filename: `79_05_05_cross_database.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Query across databases

- [ ] Multiple database tasks
- [ ] Data federation patterns
- [ ] Transfer between databases
- [ ] Consistency considerations

**Expected Behavior**: Cross-DB workflow works

---

# 79.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding SQL operator pitfalls.

## Tasks

### - [ ] 79.6.1 SQL Injection Vulnerabilities
Filename: `79_06_01_sql_injection_risks.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Prevent SQL injection

- [ ] String formatting for SQL
- [ ] Unvalidated user input
- [ ] Dynamic table names risk
- [ ] Proper parameterization

**Expected Behavior**: Injection prevented

---

### - [ ] 79.6.2 Unbounded Query Results
Filename: `79_06_02_unbounded_queries.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid memory issues with large results

- [ ] SELECT * without LIMIT
- [ ] Full table scans
- [ ] Memory exhaustion
- [ ] Pagination patterns

**Expected Behavior**: Results bounded

---

### - [ ] 79.6.3 Missing Transaction Management
Filename: `79_06_03_missing_transactions.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Handle transactions properly

- [ ] Partial updates on failure
- [ ] Missing rollback
- [ ] Autocommit confusion
- [ ] Transaction boundaries

**Expected Behavior**: Transactions managed

---

### - [ ] 79.6.4 Hardcoded Connection Strings
Filename: `79_06_04_hardcoded_connections.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Use connections properly

- [ ] Credentials in code
- [ ] Environment mismatch
- [ ] No connection abstraction
- [ ] Security risks

**Expected Behavior**: Connections used

---

### - [ ] 79.6.5 Inefficient Query Patterns
Filename: `79_06_05_inefficient_queries.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Write efficient SQL

- [ ] N+1 query problems
- [ ] Missing indexes
- [ ] Cartesian products
- [ ] Query optimization

**Expected Behavior**: Queries optimized

---

# 79.7 Testing SQL Operators

## Overview
Testing SQL-based workflows.

## Tasks

### - [ ] 79.7.1 Unit Testing SQL Logic
Filename: `79_07_01_unit_testing_sql.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test SQL logic

- [ ] Test query construction
- [ ] Validate parameters
- [ ] Assert SQL correctness
- [ ] Mock database calls

**Expected Behavior**: SQL logic tested

---

### - [ ] 79.7.2 Integration Testing with SQLite
Filename: `79_07_02_integration_sqlite.py` | Tags: `['reference', 'testing', 'beginner', 'success']`

**Purpose**: Test with SQLite

- [ ] In-memory SQLite
- [ ] Setup/teardown fixtures
- [ ] Real query execution
- [ ] Data validation

**Expected Behavior**: SQLite tests pass

---

### - [ ] 79.7.3 Docker-Based Database Testing
Filename: `79_07_03_docker_database_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test with real databases

- [ ] testcontainers usage
- [ ] PostgreSQL testing
- [ ] MySQL testing
- [ ] Database isolation

**Expected Behavior**: Real DB tests work

---

### - [ ] 79.7.4 Data Validation Testing
Filename: `79_07_04_data_validation_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Validate query results

- [ ] Expected row counts
- [ ] Data type validation
- [ ] Content assertions
- [ ] Schema validation

**Expected Behavior**: Data validated

---

### - [ ] 79.7.5 Performance Regression Testing
Filename: `79_07_05_performance_regression.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Detect query slowdowns

- [ ] Query timing benchmarks
- [ ] Execution plan analysis
- [ ] Regression detection
- [ ] Performance baselines

**Expected Behavior**: Performance tracked

---

# 79.8 Performance Optimization

## Overview
Optimizing SQL operator performance.

## Tasks

### - [ ] 79.8.1 Query Optimization Techniques
Filename: `79_08_01_query_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Write performant queries

- [ ] Index utilization
- [ ] Query plan analysis
- [ ] Subquery optimization
- [ ] Join optimization

**Expected Behavior**: Queries optimized

---

### - [ ] 79.8.2 Batch Operations
Filename: `79_08_02_batch_operations.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Efficient bulk operations

- [ ] Batch INSERT
- [ ] Batch UPDATE
- [ ] Batch DELETE
- [ ] Optimal batch sizes

**Expected Behavior**: Bulk ops efficient

---

### - [ ] 79.8.3 Connection Pool Tuning
Filename: `79_08_03_connection_pool_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize connection usage

- [ ] Pool size configuration
- [ ] Connection timeout
- [ ] Pool recycle settings
- [ ] Overflow handling

**Expected Behavior**: Connections efficient

---

### - [ ] 79.8.4 Parallel Query Execution
Filename: `79_08_04_parallel_queries.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Execute queries in parallel

- [ ] Independent query parallelism
- [ ] Task mapping for SQL
- [ ] Connection limits
- [ ] Result aggregation

**Expected Behavior**: Queries parallelized

---

### - [ ] 79.8.5 Large Data Set Handling
Filename: `79_08_05_large_data_handling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Handle big query results

- [ ] Streaming results
- [ ] Chunked processing
- [ ] Temporary tables
- [ ] Memory management

**Expected Behavior**: Large data handled

---

# 79.9 Debugging SQL Issues

## Overview
Troubleshooting SQL operator problems.

## Tasks

### - [ ] 79.9.1 Query Error Debugging
Filename: `79_09_01_query_error_debugging.py` | Tags: `['reference', 'debugging', 'beginner', 'failure']`

**Purpose**: Debug SQL syntax errors

- [ ] Error message parsing
- [ ] Query logging
- [ ] Parameter inspection
- [ ] Database-specific errors

**Expected Behavior**: Errors diagnosed

---

### - [ ] 79.9.2 Connection Debugging
Filename: `79_09_02_connection_debugging.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug connection issues

- [ ] Connection refused
- [ ] Authentication failures
- [ ] Network issues
- [ ] SSL/TLS problems

**Expected Behavior**: Connections fixed

---

### - [ ] 79.9.3 Transaction Debugging
Filename: `79_09_03_transaction_debugging.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug transaction issues

- [ ] Deadlock detection
- [ ] Lock timeouts
- [ ] Uncommitted transactions
- [ ] Isolation level issues

**Expected Behavior**: Transaction issues resolved

---

### - [ ] 79.9.4 Performance Debugging
Filename: `79_09_04_performance_debugging.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug slow queries

- [ ] EXPLAIN ANALYZE usage
- [ ] Identify bottlenecks
- [ ] Index suggestions
- [ ] Query profiling

**Expected Behavior**: Slow queries identified

---

### - [ ] 79.9.5 Data Type Issues
Filename: `79_09_05_data_type_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug type mismatches

- [ ] Type conversion errors
- [ ] NULL handling
- [ ] Encoding issues
- [ ] Precision loss

**Expected Behavior**: Type issues fixed

---

# 79.10 Real-World Examples

## Overview
Production SQL workflow patterns.

## Tasks

### - [ ] 79.10.1 Data Warehouse Loading Pipeline
Filename: `79_10_01_warehouse_loading.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Load data into warehouse

- [ ] Staging table pattern
- [ ] Upsert/merge logic
- [ ] Data transformation
- [ ] Quality checks

**Expected Behavior**: Warehouse loaded

---

### - [ ] 79.10.2 Database Maintenance Workflow
Filename: `79_10_02_database_maintenance.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Automate DB maintenance

- [ ] Index maintenance
- [ ] Statistics update
- [ ] Partition management
- [ ] Vacuum/analyze

**Expected Behavior**: DB maintained

---

### - [ ] 79.10.3 Cross-Database Data Sync
Filename: `79_10_03_cross_db_sync.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Sync between databases

- [ ] Change detection
- [ ] Incremental sync
- [ ] Conflict handling
- [ ] Validation

**Expected Behavior**: Databases synced

---

### - [ ] 79.10.4 Reporting Pipeline
Filename: `79_10_04_reporting_pipeline.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Generate reports from SQL

- [ ] Report data aggregation
- [ ] Materialized views
- [ ] Export to files
- [ ] Scheduled reporting

**Expected Behavior**: Reports generated

---

### - [ ] 79.10.5 Data Quality Validation Pipeline
Filename: `79_10_05_data_quality_validation.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Validate data quality with SQL

- [ ] Completeness checks
- [ ] Uniqueness validation
- [ ] Referential integrity
- [ ] Business rule validation

**Expected Behavior**: Quality validated

---

# Summary

## Topic Completion Checklist
- [ ] SQL execution basics covered
- [ ] Parameterized queries documented
- [ ] Result handling patterns included
- [ ] Database-specific patterns explained
- [ ] Advanced workflows provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 24: Database Providers
- Section 80: Transfer Operators
- Section 81: Connections

## Notes for Implementation
- Test with SQLite for portability
- Show parameter binding clearly
- Include error handling
- Demonstrate transactions
- Cover result processing

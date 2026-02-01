# 36 Object Storage

## Overview

Airflow's Object Storage abstraction provides a unified API for working with cloud storage systems (S3, GCS, Azure Blob) via `ObjectStoragePath`. This enables cloud-agnostic DAGs that can switch between storage providers without code changes.

## Research & Background

### Key Concepts
- **ObjectStoragePath**: Unified path abstraction for object storage (`airflow.sdk.ObjectStoragePath`)
- **Protocol Schemes**: `s3://`, `gs://`, `azure://` determine the backend
- **Connection Integration**: `conn_id` in URL or as parameter for authentication
- **fsspec Compatibility**: Exposes underlying filesystem for library integration

### Airflow 3.x Notes
- Import: `from airflow.sdk import ObjectStoragePath`
- Introduced in Airflow 2.8, refined in 3.x
- Works with TaskFlow API and traditional operators
- Provider packages required: `apache-airflow-providers-amazon[s3fs]`, `apache-airflow-providers-google`, etc.

### Prerequisites
- Airflow 3.x
- Relevant provider packages installed
- Cloud storage connections configured

---

# 36.1 ObjectStoragePath Fundamentals

### - [ ] 36.1.1 Basic ObjectStoragePath Usage
Filename: `36_01_01_basic_object_storage_path.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Introduce ObjectStoragePath for cloud-agnostic file operations

- [ ] Import from airflow.sdk
- [ ] Create path with protocol://bucket/key format
- [ ] Use conn_id for authentication
- [ ] Basic read/write operations

**Expected Behavior**: Read/write files to cloud storage using unified API

---

### - [ ] 36.1.2 S3 ObjectStoragePath
Filename: `36_01_02_s3_object_storage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use ObjectStoragePath with Amazon S3

- [ ] `ObjectStoragePath("s3://aws_default@bucket/path/")`
- [ ] S3 connection configuration
- [ ] Read, write, list operations
- [ ] Requires apache-airflow-providers-amazon[s3fs]

**Expected Behavior**: S3 operations via unified API

---

### - [ ] 36.1.3 GCS ObjectStoragePath
Filename: `36_01_03_gcs_object_storage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use ObjectStoragePath with Google Cloud Storage

- [ ] `ObjectStoragePath("gs://gcp_conn@bucket/path/")`
- [ ] GCS connection configuration
- [ ] Read, write, list operations
- [ ] Requires apache-airflow-providers-google

**Expected Behavior**: GCS operations via unified API

---

### - [ ] 36.1.4 Azure Blob ObjectStoragePath
Filename: `36_01_04_azure_object_storage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use ObjectStoragePath with Azure Blob Storage

- [ ] `ObjectStoragePath("azure://azure_conn@container/path/")`
- [ ] Azure connection configuration
- [ ] Read, write, list operations
- [ ] Requires apache-airflow-providers-microsoft-azure

**Expected Behavior**: Azure Blob operations via unified API

---

### - [ ] 36.1.5 Connection ID Patterns
Filename: `36_01_05_connection_patterns.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Different ways to specify authentication

- [ ] conn_id in URL: `s3://my_conn@bucket/`
- [ ] conn_id as parameter: `ObjectStoragePath("s3://bucket/", conn_id="my_conn")`
- [ ] Default connection fallback
- [ ] Environment-specific connections

**Expected Behavior**: Flexible authentication patterns

---

# 36.2 File Operations

### - [ ] 36.2.1 Reading Files
Filename: `36_02_01_reading_files.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Read files from object storage

- [ ] `path.read_text()` for text files
- [ ] `path.read_bytes()` for binary files
- [ ] Context manager with `path.open("r")`
- [ ] Streaming large files

**Expected Behavior**: File content retrieved from cloud storage

---

### - [ ] 36.2.2 Writing Files
Filename: `36_02_02_writing_files.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Write files to object storage

- [ ] `path.write_text(content)`
- [ ] `path.write_bytes(data)`
- [ ] Context manager with `path.open("w")`
- [ ] Overwrite behavior

**Expected Behavior**: Files created in cloud storage

---

### - [ ] 36.2.3 Listing Files
Filename: `36_02_03_listing_files.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: List files and directories in object storage

- [ ] `path.iterdir()` for immediate children
- [ ] `path.glob("*.parquet")` for pattern matching
- [ ] `path.rglob("**/*.csv")` for recursive search
- [ ] Handling large listings

**Expected Behavior**: File listings from cloud storage

---

### - [ ] 36.2.4 File Metadata
Filename: `36_02_04_file_metadata.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Access file metadata and properties

- [ ] `path.exists()` check
- [ ] `path.stat()` for size, modified time
- [ ] `path.is_file()` / `path.is_dir()`
- [ ] Provider-specific metadata

**Expected Behavior**: File metadata accessible via unified API

---

### - [ ] 36.2.5 Path Manipulation
Filename: `36_02_05_path_manipulation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Manipulate paths like pathlib

- [ ] `base / "subdir" / "file.txt"` joining
- [ ] `path.parent` / `path.name` / `path.suffix`
- [ ] `path.with_suffix(".parquet")`
- [ ] Relative path operations

**Expected Behavior**: Intuitive path manipulation

---

# 36.3 Advanced Operations

### - [ ] 36.3.1 Cross-Storage Copy
Filename: `36_03_01_cross_storage_copy.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Copy files between different storage providers

- [ ] S3 to GCS transfer
- [ ] Local to cloud upload
- [ ] Cloud to local download
- [ ] Streaming for large files

**Expected Behavior**: Files transferred between storage systems

---

### - [ ] 36.3.2 Directory Operations
Filename: `36_03_02_directory_operations.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Bulk operations on directories

- [ ] Copy entire directories
- [ ] Delete directories recursively
- [ ] Sync directories
- [ ] shutil integration

**Expected Behavior**: Directory-level operations work across providers

---

### - [ ] 36.3.3 fsspec Integration
Filename: `36_03_03_fsspec_integration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Access underlying fsspec filesystem

- [ ] `path.fs` property for fsspec filesystem
- [ ] Use with pandas, DuckDB, PyArrow
- [ ] Apache Iceberg integration
- [ ] Dask integration

**Expected Behavior**: ObjectStoragePath works with fsspec-compatible libraries

---

### - [ ] 36.3.4 Templated Paths
Filename: `36_03_04_templated_paths.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Use Jinja templating with ObjectStoragePath

- [ ] Date-partitioned paths: `s3://bucket/data/{{ ds }}/`
- [ ] Dynamic path construction
- [ ] TaskFlow with templated paths
- [ ] Backfill considerations

**Expected Behavior**: Dynamic paths based on execution context

---

### - [ ] 36.3.5 Error Handling
Filename: `36_03_05_error_handling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle object storage errors gracefully

- [ ] FileNotFoundError handling
- [ ] Permission errors
- [ ] Network/timeout errors
- [ ] Retry patterns

**Expected Behavior**: Robust error handling for cloud operations

---

# 36.4 XCom Object Storage Backend

### - [ ] 36.4.1 Configure XCom Object Storage
Filename: `36_04_01_xcom_object_storage.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Store large XCom values in object storage

- [ ] Configure xcom_backend setting
- [ ] S3 XCom backend setup
- [ ] GCS XCom backend setup
- [ ] Size threshold configuration

**Expected Behavior**: Large XCom values stored in cloud storage

---

### - [ ] 36.4.2 Custom XCom Backend
Filename: `36_04_02_custom_xcom_backend.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Implement custom XCom storage backend

- [ ] Extend BaseXCom class
- [ ] Serialize/deserialize methods
- [ ] Custom storage location logic
- [ ] Compression options

**Expected Behavior**: Custom XCom storage implementation

---

### - [ ] 36.4.3 XCom Cleanup
Filename: `36_04_03_xcom_cleanup.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Manage XCom storage lifecycle

- [ ] Automatic cleanup policies
- [ ] Manual cleanup tasks
- [ ] Retention configuration
- [ ] Storage cost management

**Expected Behavior**: XCom storage properly managed

---

### - [ ] 36.4.4 XCom with ObjectStoragePath
Filename: `36_04_04_xcom_with_osp.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Return ObjectStoragePath from tasks

- [ ] Return path reference in XCom
- [ ] Downstream task reads from path
- [ ] Avoid serializing large data
- [ ] Pattern for data handoff

**Expected Behavior**: Efficient data passing via path references

---

### - [ ] 36.4.5 Multi-Backend XCom
Filename: `36_04_05_multi_backend_xcom.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Different XCom backends for different use cases

- [ ] Small values in metadata DB
- [ ] Large values in object storage
- [ ] Task-specific backend selection
- [ ] Migration strategies

**Expected Behavior**: Optimized XCom storage per use case

---

# 36.5 Remote Logging

### - [ ] 36.5.1 S3 Remote Logging
Filename: `36_05_01_s3_remote_logging.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Store Airflow logs in S3

- [ ] Configure remote_logging = True
- [ ] Set remote_log_conn_id
- [ ] S3 bucket and path configuration
- [ ] Log reading from UI

**Expected Behavior**: Task logs stored in and read from S3

---

### - [ ] 36.5.2 GCS Remote Logging
Filename: `36_05_02_gcs_remote_logging.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Store Airflow logs in GCS

- [ ] GCS logging configuration
- [ ] Bucket permissions setup
- [ ] Path pattern configuration
- [ ] Log retention

**Expected Behavior**: Task logs stored in and read from GCS

---

### - [ ] 36.5.3 Azure Blob Remote Logging
Filename: `36_05_03_azure_remote_logging.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Store Airflow logs in Azure Blob Storage

- [ ] Azure logging configuration
- [ ] Container setup
- [ ] SAS token vs connection string
- [ ] Log access from UI

**Expected Behavior**: Task logs stored in Azure Blob

---

### - [ ] 36.5.4 Log Encryption
Filename: `36_05_04_log_encryption.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Encrypt logs in object storage

- [ ] Server-side encryption (SSE)
- [ ] Customer-managed keys
- [ ] KMS integration
- [ ] Compliance requirements

**Expected Behavior**: Logs encrypted at rest

---

### - [ ] 36.5.5 Log Lifecycle Management
Filename: `36_05_05_log_lifecycle.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Manage log storage lifecycle

- [ ] Retention policies
- [ ] Archive to cold storage
- [ ] Automatic deletion
- [ ] Cost optimization

**Expected Behavior**: Log storage costs managed effectively

---

# 36.6 Best Practices

### - [ ] 36.6.1 Provider-Agnostic DAGs
Filename: `36_06_01_provider_agnostic.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Write DAGs that work with any storage provider

- [ ] Parameterize protocol in Variables
- [ ] Environment-based connection selection
- [ ] Testing with different backends
- [ ] Migration strategies

**Expected Behavior**: Same DAG code works with S3, GCS, or Azure

---

### - [ ] 36.6.2 Performance Optimization
Filename: `36_06_02_performance.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Optimize object storage operations

- [ ] Batch operations
- [ ] Parallel downloads/uploads
- [ ] Streaming for large files
- [ ] Caching strategies

**Expected Behavior**: Efficient object storage operations

---

### - [ ] 36.6.3 Security Best Practices
Filename: `36_06_03_security.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Secure object storage access

- [ ] Principle of least privilege
- [ ] Bucket policies
- [ ] Encryption at rest/transit
- [ ] Audit logging

**Expected Behavior**: Secure object storage configuration

---

### - [ ] 36.6.4 Cost Management
Filename: `36_06_04_cost_management.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Control object storage costs

- [ ] Storage class selection
- [ ] Lifecycle policies
- [ ] Data transfer costs
- [ ] Monitoring usage

**Expected Behavior**: Cost-effective storage usage

---

### - [ ] 36.6.5 Testing Object Storage
Filename: `36_06_05_testing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Test DAGs with object storage

- [ ] LocalStack for S3 testing
- [ ] GCS emulator
- [ ] Azurite for Azure
- [ ] Mock ObjectStoragePath

**Expected Behavior**: Reliable testing without cloud dependencies

---

# Summary

## Topic Completion Checklist
- [ ] ObjectStoragePath fundamentals covered
- [ ] All major cloud providers included (S3, GCS, Azure)
- [ ] XCom backend configuration documented
- [ ] Remote logging setup for all providers
- [ ] Best practices and testing strategies

## Related Topics
- Section 07: XCom (data passing basics)
- Section 21: AWS Providers (S3 operators)
- Section 22: GCP Providers (GCS operators)
- Section 23: Azure Providers (Blob operators)
- Section 19: Logging & Monitoring

## Notes for Implementation
- Install provider packages with extras: `apache-airflow-providers-amazon[s3fs]`
- Test with local emulators before cloud deployment
- Use templated paths for date-partitioned data

---

# 36.7 Advanced ObjectStoragePath Patterns

### - [ ] 36.7.1 Partitioned Data Access
Filename: `36_07_01_partitioned_data.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Work with date-partitioned data layouts
- [ ] Generate partition paths dynamically
- [ ] Handle missing partitions gracefully
- [ ] Optimize partition discovery

### - [ ] 36.7.2 Atomic File Operations
Filename: `36_07_02_atomic_operations.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Write to temp location then rename
- [ ] Handle partial write failures
- [ ] Implement check-then-write pattern
- [ ] Ensure idempotent file creation

### - [ ] 36.7.3 Large File Handling
Filename: `36_07_03_large_files.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Stream large files without loading to memory
- [ ] Multipart uploads for large objects
- [ ] Resume interrupted transfers
- [ ] Handle timeout for large operations

### - [ ] 36.7.4 Concurrent File Operations
Filename: `36_07_04_concurrent_operations.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Parallel downloads using threads
- [ ] Batch uploads with concurrency limits
- [ ] Handle rate limiting
- [ ] Coordinate file access across tasks

### - [ ] 36.7.5 Data Format Integration
Filename: `36_07_05_data_format_integration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Read/write Parquet with ObjectStoragePath
- [ ] Handle CSV, JSON, Avro formats
- [ ] Integrate with pandas/DuckDB
- [ ] Schema evolution handling

---

# 36.8 Object Storage Debugging

### - [ ] 36.8.1 Debug Permission Errors
Filename: `36_08_01_debug_permissions.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

- [ ] Troubleshoot access denied errors
- [ ] Verify IAM/service account permissions
- [ ] Debug cross-account access issues
- [ ] Handle bucket policy conflicts

### - [ ] 36.8.2 Debug Connectivity Issues
Filename: `36_08_02_debug_connectivity.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

- [ ] Diagnose timeout errors
- [ ] Handle VPC endpoint issues
- [ ] Debug proxy configuration
- [ ] Test network connectivity

### - [ ] 36.8.3 Debug Encoding Issues
Filename: `36_08_03_debug_encoding.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

- [ ] Handle unicode filename issues
- [ ] Debug content type problems
- [ ] Fix binary vs text mode errors
- [ ] Handle special characters in keys

### - [ ] 36.8.4 Debug Performance Issues
Filename: `36_08_04_debug_performance.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

- [ ] Identify slow operations
- [ ] Profile ObjectStoragePath calls
- [ ] Debug throttling issues
- [ ] Optimize listing operations

### - [ ] 36.8.5 Common Object Storage Pitfalls
Filename: `36_08_05_common_pitfalls.py` | Tags: `['reference', 'anti-patterns', 'intermediate', 'failure']`

- [ ] Avoid listing millions of objects
- [ ] Handle eventual consistency
- [ ] Prevent connection leaks
- [ ] Fix path normalization bugs

---

# 36.9 Multi-Cloud and Hybrid Storage

### - [ ] 36.9.1 Multi-Cloud Data Movement
Filename: `36_09_01_multi_cloud_movement.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Transfer data between cloud providers
- [ ] Handle authentication across providers
- [ ] Optimize cross-cloud transfers
- [ ] Manage costs for egress

### - [ ] 36.9.2 Hybrid Cloud Storage
Filename: `36_09_02_hybrid_storage.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Integrate on-premises storage
- [ ] Use MinIO for local development
- [ ] Handle network latency differences
- [ ] Implement tiered storage

### - [ ] 36.9.3 Cloud-Agnostic DAG Design
Filename: `36_09_03_cloud_agnostic_design.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Abstract storage provider details
- [ ] Use Variables for provider selection
- [ ] Support runtime provider switching
- [ ] Test across all target providers

### - [ ] 36.9.4 Data Replication Patterns
Filename: `36_09_04_data_replication.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Replicate data across regions
- [ ] Implement sync vs async replication
- [ ] Handle conflict resolution
- [ ] Monitor replication lag

### - [ ] 36.9.5 Disaster Recovery Storage
Filename: `36_09_05_disaster_recovery.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Configure cross-region backups
- [ ] Test failover procedures
- [ ] Handle data consistency
- [ ] Document recovery steps

---

# 36.10 Real-World Object Storage Examples

### - [ ] 36.10.1 Data Lake Pipeline
Filename: `36_10_01_data_lake_pipeline.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`

- [ ] Ingest data to raw layer
- [ ] Transform to processed layer
- [ ] Organize with standard partitioning
- [ ] Handle late-arriving data

### - [ ] 36.10.2 ETL with Object Storage
Filename: `36_10_02_etl_object_storage.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`

- [ ] Extract from source systems to storage
- [ ] Transform using Spark/pandas
- [ ] Load to analytics layer
- [ ] Manage intermediate files

### - [ ] 36.10.3 ML Pipeline Data Management
Filename: `36_10_03_ml_data_management.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`

- [ ] Store training datasets
- [ ] Version model artifacts
- [ ] Handle feature store integration
- [ ] Manage experiment outputs

### - [ ] 36.10.4 Log Archive Pipeline
Filename: `36_10_04_log_archive_pipeline.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`

- [ ] Collect and compress logs
- [ ] Partition by date
- [ ] Apply lifecycle policies
- [ ] Enable efficient querying

### - [ ] 36.10.5 Media Processing Pipeline
Filename: `36_10_05_media_processing.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`

- [ ] Handle large media files
- [ ] Process images/videos in tasks
- [ ] Store multiple renditions
- [ ] Manage content delivery

<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 -->

# 75 Docker Operators

## Overview
Using DockerOperator and related operators for containerized task execution including image management, volume mounting, and network configuration.

---

# 75.1 DockerOperator Basics

### - [ ] 75.1.1 Basic DockerOperator
Filename: `75_01_01_basic.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] image parameter
- [ ] command parameter
- [ ] Task instantiation
- [ ] Container lifecycle

### - [ ] 75.1.2 Image Selection
Filename: `75_01_02_image.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Image tags
- [ ] Registry references
- [ ] Latest vs pinned
- [ ] Image pull policy

### - [ ] 75.1.3 Container Commands
Filename: `75_01_03_commands.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Command string
- [ ] Entrypoint override
- [ ] Shell execution
- [ ] Multi-command

### - [ ] 75.1.4 Environment Variables
Filename: `75_01_04_environment.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] environment parameter
- [ ] Secret handling
- [ ] Template variables
- [ ] Env file support

### - [ ] 75.1.5 Container Networking
Filename: `75_01_05_networking.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] network_mode parameter
- [ ] Bridge vs host
- [ ] Custom networks
- [ ] Port mapping

---

# 75.2 Volume and Storage

### - [ ] 75.2.1 Volume Mounting
Filename: `75_02_01_volumes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] mounts parameter
- [ ] Bind mounts
- [ ] Named volumes
- [ ] Permission handling

### - [ ] 75.2.2 Temp Directories
Filename: `75_02_02_temp_dir.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] tmp_dir parameter
- [ ] Auto-cleanup
- [ ] Shared temp
- [ ] Use cases

### - [ ] 75.2.3 Data Sharing
Filename: `75_02_03_data_sharing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Host to container
- [ ] Container to host
- [ ] Between tasks
- [ ] XCom alternatives

### - [ ] 75.2.4 Config File Injection
Filename: `75_02_04_config_injection.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Mount config files
- [ ] Template configs
- [ ] Secret configs
- [ ] Override patterns

### - [ ] 75.2.5 Persistent Storage
Filename: `75_02_05_persistent.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Persistent volumes
- [ ] Volume lifecycle
- [ ] Cleanup strategies
- [ ] State management

---

# 75.3 Container Configuration

### - [ ] 75.3.1 Resource Limits
Filename: `75_03_01_resources.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] mem_limit parameter
- [ ] cpu_shares/cpu_period
- [ ] shm_size
- [ ] Resource constraints

### - [ ] 75.3.2 Container User
Filename: `75_03_02_user.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] user parameter
- [ ] UID/GID mapping
- [ ] Root vs non-root
- [ ] Permission issues

### - [ ] 75.3.3 Privileged Mode
Filename: `75_03_03_privileged.py` | Tags: `['reference', 'core', 'advanced', 'success']`
- [ ] privileged parameter
- [ ] Security implications
- [ ] When needed
- [ ] Alternatives

### - [ ] 75.3.4 Container Capabilities
Filename: `75_03_04_capabilities.py` | Tags: `['reference', 'core', 'advanced', 'success']`
- [ ] cap_add parameter
- [ ] cap_drop parameter
- [ ] Security hardening
- [ ] Minimal capabilities

### - [ ] 75.3.5 Docker Socket Access
Filename: `75_03_05_socket.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Docker-in-Docker
- [ ] Socket mounting
- [ ] Security risks
- [ ] Use cases

---

# 75.4 Output and Logging

### - [ ] 75.4.1 Container Output
Filename: `75_04_01_output.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Log streaming
- [ ] Output capture
- [ ] XCom from output
- [ ] Output parsing

### - [ ] 75.4.2 Logging Configuration
Filename: `75_04_02_logging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] auto_remove parameter
- [ ] Log driver
- [ ] Log retention
- [ ] Debugging

### - [ ] 75.4.3 Exit Code Handling
Filename: `75_04_03_exit_codes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Container exit codes
- [ ] Success/failure detection
- [ ] Custom handling
- [ ] Retry behavior

### - [ ] 75.4.4 Container Inspection
Filename: `75_04_04_inspection.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Container state
- [ ] Metadata access
- [ ] Debug information
- [ ] Post-mortem analysis

### - [ ] 75.4.5 Output as XCom
Filename: `75_04_05_xcom.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] xcom_push parameter
- [ ] Output format
- [ ] Size limitations
- [ ] Parsing patterns

---

# 75.5 Advanced Docker Patterns

### - [ ] 75.5.1 Dynamic Image Selection
Filename: `75_05_01_dynamic_image.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Templated image
- [ ] Version selection
- [ ] Environment-based
- [ ] XCom image

### - [ ] 75.5.2 Multi-Container Patterns
Filename: `75_05_02_multi_container.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Sidecar containers
- [ ] Init containers
- [ ] Container coordination
- [ ] Shared state

### - [ ] 75.5.3 Docker Registry Auth
Filename: `75_05_03_registry_auth.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] docker_conn_id
- [ ] Registry credentials
- [ ] Private registries
- [ ] ECR/GCR/ACR

### - [ ] 75.5.4 GPU Support
Filename: `75_05_04_gpu.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] device_requests
- [ ] NVIDIA runtime
- [ ] GPU allocation
- [ ] ML workloads

### - [ ] 75.5.5 Docker Task Testing
Filename: `75_05_05_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Mock Docker
- [ ] Container verification
- [ ] Integration tests
- [ ] CI/CD setup

---

# 75.6 Docker Operator Anti-Patterns

### - [ ] 75.6.1 Latest Tag Usage
Filename: `75_06_01_latest_tag.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Reproducibility issues
- [ ] Silent changes
- [ ] Version pinning
- [ ] Tag strategies

### - [ ] 75.6.2 Privileged Mode Abuse
Filename: `75_06_02_privileged_abuse.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Security risks
- [ ] Container escape
- [ ] Minimal capabilities
- [ ] Alternatives

### - [ ] 75.6.3 Large Container Images
Filename: `75_06_03_large_images.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Pull time impact
- [ ] Storage costs
- [ ] Multi-stage builds
- [ ] Image optimization

### - [ ] 75.6.4 Ignoring Container Cleanup
Filename: `75_06_04_no_cleanup.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Resource leaks
- [ ] Disk exhaustion
- [ ] Auto-remove usage
- [ ] Cleanup patterns

### - [ ] 75.6.5 Hardcoded Configuration
Filename: `75_06_05_hardcoded_config.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Environment inflexibility
- [ ] Secret exposure
- [ ] Configuration injection
- [ ] Best practices

---

# 75.7 Docker Operator Performance

### - [ ] 75.7.1 Image Pull Optimization
Filename: `75_07_01_image_pull.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Pull policies
- [ ] Local caching
- [ ] Registry proximity
- [ ] Pre-pulling strategies

### - [ ] 75.7.2 Container Startup Time
Filename: `75_07_02_startup_time.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Startup optimization
- [ ] Init process
- [ ] Health check tuning
- [ ] Warm containers

### - [ ] 75.7.3 Resource Allocation
Filename: `75_07_03_resource_allocation.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] CPU/memory limits
- [ ] Right-sizing
- [ ] Overcommit patterns
- [ ] Performance tuning

### - [ ] 75.7.4 Volume Performance
Filename: `75_07_04_volume_perf.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Mount performance
- [ ] Volume drivers
- [ ] IO optimization
- [ ] Caching strategies

### - [ ] 75.7.5 Network Performance
Filename: `75_07_05_network_perf.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Network modes
- [ ] DNS resolution
- [ ] Connection pooling
- [ ] Latency optimization

---

# 75.8 Docker Operator Debugging

### - [ ] 75.8.1 Container Inspection
Filename: `75_08_01_container_inspection.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Container logs
- [ ] State inspection
- [ ] Resource usage
- [ ] Process listing

### - [ ] 75.8.2 Image Debugging
Filename: `75_08_02_image_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Image inspection
- [ ] Layer analysis
- [ ] Entrypoint debugging
- [ ] Environment verification

### - [ ] 75.8.3 Network Debugging
Filename: `75_08_03_network_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Connectivity issues
- [ ] DNS problems
- [ ] Port mapping
- [ ] Network inspection

### - [ ] 75.8.4 Volume Debugging
Filename: `75_08_04_volume_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Mount verification
- [ ] Permission issues
- [ ] Path problems
- [ ] Content inspection

### - [ ] 75.8.5 Exit Code Analysis
Filename: `75_08_05_exit_code.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Exit code meanings
- [ ] Signal analysis
- [ ] OOM detection
- [ ] Error identification

---

# 75.9 Real-World Docker Operator Examples

### - [ ] 75.9.1 Data Processing Container
Filename: `75_09_01_data_processing.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] ETL containers
- [ ] Volume mounting
- [ ] Result extraction
- [ ] Error handling

### - [ ] 75.9.2 ML Training Container
Filename: `75_09_02_ml_training.py` | Tags: `['reference', 'example', 'advanced', 'success']`
- [ ] GPU allocation
- [ ] Model storage
- [ ] Hyperparameter passing
- [ ] Checkpoint handling

### - [ ] 75.9.3 Testing Container
Filename: `75_09_03_testing_container.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] Test execution
- [ ] Coverage collection
- [ ] Report generation
- [ ] Artifact handling

### - [ ] 75.9.4 Build Container
Filename: `75_09_04_build_container.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] Build process
- [ ] Artifact extraction
- [ ] Cache utilization
- [ ] Multi-stage patterns

### - [ ] 75.9.5 Database Migration Container
Filename: `75_09_05_db_migration.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] Migration execution
- [ ] Connection handling
- [ ] Rollback support
- [ ] State verification

---

# 75.10 Docker Operator Best Practices

### - [ ] 75.10.1 Image Management
Filename: `75_10_01_image_management.py` | Tags: `['reference', 'best-practice', 'beginner', 'success']`
- [ ] Version tagging
- [ ] Registry organization
- [ ] Cleanup policies
- [ ] Security scanning

### - [ ] 75.10.2 Security Best Practices
Filename: `75_10_02_security.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`
- [ ] Minimal privileges
- [ ] Secret handling
- [ ] Image provenance
- [ ] Network isolation

### - [ ] 75.10.3 Resource Management
Filename: `75_10_03_resource_management.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`
- [ ] Limit configuration
- [ ] Cleanup automation
- [ ] Monitoring setup
- [ ] Capacity planning

### - [ ] 75.10.4 Configuration Management
Filename: `75_10_04_configuration.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`
- [ ] Environment variables
- [ ] Config injection
- [ ] Secret management
- [ ] Template patterns

### - [ ] 75.10.5 Documentation Standards
Filename: `75_10_05_documentation.py` | Tags: `['reference', 'best-practice', 'beginner', 'success']`
- [ ] Image documentation
- [ ] Environment requirements
- [ ] Volume specifications
- [ ] Troubleshooting guides

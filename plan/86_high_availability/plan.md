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

# 86 High Availability

## Overview

High availability (HA) configuration ensures Airflow continues operating during component failures. Airflow 3.x supports scheduler HA, database replication, and failover strategies for production-critical deployments.

## Airflow 3.x Notes
- Native scheduler HA support
- Improved database failover handling
- Triggerer HA configuration
- Enhanced health check endpoints
- Graceful degradation patterns

---

# 86.1 Scheduler High Availability

## Overview
Running multiple schedulers for fault tolerance.

## Tasks

### - [ ] 86.1.1 Multiple Scheduler Setup
Filename: `86_01_01_multiple_schedulers.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure multiple active schedulers

- [ ] Scheduler configuration for HA
- [ ] Database row-level locking
- [ ] Scheduler synchronization
- [ ] Load distribution

**Expected Behavior**: Multiple schedulers work together

---

### - [ ] 86.1.2 Scheduler Failover Detection
Filename: `86_01_02_scheduler_failover.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Detect and handle scheduler failures

- [ ] Heartbeat monitoring
- [ ] scheduler_health_check_threshold
- [ ] Automatic failover behavior
- [ ] Manual failover procedures

**Expected Behavior**: Failover works seamlessly

---

### - [ ] 86.1.3 Scheduler Health Checks
Filename: `86_01_03_scheduler_health_checks.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Monitor scheduler health

- [ ] Health check endpoints
- [ ] Liveness and readiness probes
- [ ] Kubernetes probe configuration
- [ ] Load balancer health checks

**Expected Behavior**: Health properly monitored

---

### - [ ] 86.1.4 DAG Parsing Distribution
Filename: `86_01_04_dag_parsing_distribution.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Distribute DAG parsing load

- [ ] DAG processor HA
- [ ] Parsing lock management
- [ ] File-based locking
- [ ] Parsing throughput optimization

**Expected Behavior**: Parsing distributed efficiently

---

### - [ ] 86.1.5 Scheduler Conflict Resolution
Filename: `86_01_05_scheduler_conflicts.py` | Tags: `['reference', 'core', 'advanced', 'failure']`

**Purpose**: Handle scheduler conflicts

- [ ] Task adoption scenarios
- [ ] Orphaned task handling
- [ ] Duplicate execution prevention
- [ ] Conflict logging and alerts

**Expected Behavior**: Conflicts resolved gracefully

---

# 86.2 Database High Availability

## Overview
Database HA strategies for Airflow metadata.

## Tasks

### - [ ] 86.2.1 PostgreSQL HA with Patroni
Filename: `86_02_01_postgresql_patroni.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: PostgreSQL HA cluster

- [ ] Patroni cluster setup
- [ ] Automatic failover
- [ ] Connection string configuration
- [ ] Synchronous replication

**Expected Behavior**: Database highly available

---

### - [ ] 86.2.2 MySQL/MariaDB HA Configuration
Filename: `86_02_02_mysql_ha.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: MySQL high availability

- [ ] Galera cluster setup
- [ ] Replication configuration
- [ ] ProxySQL integration
- [ ] Failover handling

**Expected Behavior**: MySQL HA working

---

### - [ ] 86.2.3 Cloud Database HA Options
Filename: `86_02_03_cloud_database_ha.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Use cloud-managed HA databases

- [ ] AWS RDS Multi-AZ
- [ ] GCP Cloud SQL HA
- [ ] Azure Database HA
- [ ] Automatic failover behavior

**Expected Behavior**: Cloud DB failover works

---

### - [ ] 86.2.4 Database Connection Pooling
Filename: `86_02_04_connection_pooling.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Optimize database connections

- [ ] PgBouncer configuration
- [ ] Pool sizing strategies
- [ ] Connection timeout handling
- [ ] Pool monitoring

**Expected Behavior**: Efficient connection management

---

### - [ ] 86.2.5 Database Backup and Recovery
Filename: `86_02_05_backup_recovery.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Database backup strategies

- [ ] Point-in-time recovery
- [ ] Backup automation
- [ ] Recovery procedures
- [ ] Backup validation

**Expected Behavior**: Recovery works reliably

---

# 86.3 Worker High Availability

## Overview
Ensuring worker availability and task continuity.

## Tasks

### - [ ] 86.3.1 Celery Worker HA
Filename: `86_03_01_celery_worker_ha.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Highly available Celery workers

- [ ] Multiple worker deployment
- [ ] Broker failover
- [ ] Task retry on worker failure
- [ ] Worker scaling automation

**Expected Behavior**: Workers highly available

---

### - [ ] 86.3.2 Kubernetes Worker Resilience
Filename: `86_03_02_k8s_worker_resilience.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: K8s pod resilience

- [ ] Pod disruption budgets
- [ ] Node affinity/anti-affinity
- [ ] Preemption handling
- [ ] Spot/preemptible instances

**Expected Behavior**: Pod failures handled

---

### - [ ] 86.3.3 Task State Recovery
Filename: `86_03_03_task_state_recovery.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Recover task state after failures

- [ ] Task adoption mechanism
- [ ] Zombie task detection
- [ ] State reconciliation
- [ ] Manual intervention procedures

**Expected Behavior**: Task state recovered

---

### - [ ] 86.3.4 Worker Queue Failover
Filename: `86_03_04_queue_failover.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle queue failures

- [ ] Redis sentinel configuration
- [ ] RabbitMQ clustering
- [ ] Queue mirroring
- [ ] Failover procedures

**Expected Behavior**: Queue failover works

---

### - [ ] 86.3.5 Worker Auto-Scaling
Filename: `86_03_05_worker_autoscaling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Automatic worker scaling

- [ ] KEDA integration
- [ ] Celery flower metrics
- [ ] Scale-to-zero patterns
- [ ] Scale-up latency optimization

**Expected Behavior**: Workers scale automatically

---

# 86.4 Webserver High Availability

## Overview
Ensuring webserver availability.

## Tasks

### - [ ] 86.4.1 Multiple Webserver Instances
Filename: `86_04_01_multiple_webservers.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Run multiple webservers

- [ ] Stateless webserver design
- [ ] Session management
- [ ] Load balancer configuration
- [ ] Sticky sessions (if needed)

**Expected Behavior**: Webservers load balanced

---

### - [ ] 86.4.2 Load Balancer Configuration
Filename: `86_04_02_load_balancer.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Configure load balancing

- [ ] Health check endpoints
- [ ] SSL termination
- [ ] Path-based routing
- [ ] Rate limiting

**Expected Behavior**: Load balancer working

---

### - [ ] 86.4.3 Session Management for HA
Filename: `86_04_03_session_management.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle sessions across instances

- [ ] Redis session backend
- [ ] Session timeout configuration
- [ ] Session security
- [ ] Graceful session migration

**Expected Behavior**: Sessions persist across instances

---

### - [ ] 86.4.4 Webserver Health Monitoring
Filename: `86_04_04_webserver_monitoring.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Monitor webserver health

- [ ] Health check implementation
- [ ] Response time monitoring
- [ ] Error rate tracking
- [ ] Automatic restart policies

**Expected Behavior**: Webserver health visible

---

### - [ ] 86.4.5 CDN and Caching Strategies
Filename: `86_04_05_cdn_caching.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Improve availability with caching

- [ ] Static asset caching
- [ ] CDN configuration
- [ ] Cache invalidation
- [ ] API response caching

**Expected Behavior**: Caching improves performance

---

# 86.5 Disaster Recovery

## Overview
Planning and implementing disaster recovery.

## Tasks

### - [ ] 86.5.1 DR Planning for Airflow
Filename: `86_05_01_dr_planning.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Disaster recovery planning

- [ ] RTO and RPO definitions
- [ ] Critical component identification
- [ ] Recovery procedures documentation
- [ ] DR testing schedule

**Expected Behavior**: DR plan documented

---

### - [ ] 86.5.2 Cross-Region Replication
Filename: `86_05_02_cross_region_replication.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Replicate across regions

- [ ] Database replication setup
- [ ] DAG synchronization
- [ ] Connection/variable sync
- [ ] Activation procedures

**Expected Behavior**: Cross-region ready

---

### - [ ] 86.5.3 Backup and Restore Procedures
Filename: `86_05_03_backup_restore.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Complete backup/restore

- [ ] Database backups
- [ ] Configuration backups
- [ ] DAG repository backups
- [ ] Restore testing

**Expected Behavior**: Restore works reliably

---

### - [ ] 86.5.4 Failover Testing
Filename: `86_05_04_failover_testing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Test failover procedures

- [ ] Chaos engineering approach
- [ ] Component failure simulation
- [ ] Recovery time measurement
- [ ] Runbook validation

**Expected Behavior**: Failover tested regularly

---

### - [ ] 86.5.5 Graceful Degradation Patterns
Filename: `86_05_05_graceful_degradation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Degrade gracefully under failures

- [ ] Component isolation
- [ ] Feature flags for degradation
- [ ] Priority queue handling
- [ ] User communication

**Expected Behavior**: System degrades gracefully

---

# 86.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding HA implementation pitfalls.

## Tasks

### - [ ] 86.6.1 Single Point of Failure
Filename: `86_06_01_single_point_failure.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Eliminate SPOFs

- [ ] Identify all SPOFs
- [ ] Database SPOF
- [ ] Scheduler SPOF
- [ ] Network SPOF

**Expected Behavior**: SPOFs eliminated

---

### - [ ] 86.6.2 Untested Failover
Filename: `86_06_02_untested_failover.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Test failover regularly

- [ ] Assumed working failover
- [ ] First test in disaster
- [ ] Configuration drift
- [ ] Regular testing schedule

**Expected Behavior**: Failover tested

---

### - [ ] 86.6.3 Over-Reliance on Auto-Recovery
Filename: `86_06_03_over_reliance_auto.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Plan for manual recovery

- [ ] Automation failures
- [ ] Edge cases
- [ ] Manual runbooks
- [ ] Human intervention procedures

**Expected Behavior**: Manual procedures ready

---

### - [ ] 86.6.4 Insufficient Redundancy
Filename: `86_06_04_insufficient_redundancy.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Plan for multiple failures

- [ ] N+1 not enough
- [ ] Cascading failures
- [ ] Capacity under failure
- [ ] N+2 patterns

**Expected Behavior**: Proper redundancy

---

### - [ ] 86.6.5 Missing Observability
Filename: `86_06_05_missing_observability.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Monitor HA status

- [ ] No failover alerts
- [ ] Silent degradation
- [ ] Health blind spots
- [ ] Comprehensive monitoring

**Expected Behavior**: HA monitored

---

# 86.7 Testing High Availability

## Overview
Testing HA configurations and failover.

## Tasks

### - [ ] 86.7.1 Chaos Engineering for Airflow
Filename: `86_07_01_chaos_engineering.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Inject failures deliberately

- [ ] Chaos Monkey patterns
- [ ] Component failure injection
- [ ] Network partition testing
- [ ] Automated chaos tests

**Expected Behavior**: Chaos tests pass

---

### - [ ] 86.7.2 Scheduler Failover Testing
Filename: `86_07_02_scheduler_failover_test.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test scheduler failover

- [ ] Kill active scheduler
- [ ] Measure takeover time
- [ ] Verify task continuity
- [ ] Validate no duplicate runs

**Expected Behavior**: Scheduler failover works

---

### - [ ] 86.7.3 Database Failover Testing
Filename: `86_07_03_database_failover_test.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test database failover

- [ ] Trigger DB failover
- [ ] Connection recovery
- [ ] Data consistency
- [ ] Application recovery

**Expected Behavior**: DB failover works

---

### - [ ] 86.7.4 Load Testing Under Failure
Filename: `86_07_04_load_under_failure.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Test load during failures

- [ ] Sustained load
- [ ] Component failure
- [ ] Performance impact
- [ ] Recovery behavior

**Expected Behavior**: Load handled under failure

---

### - [ ] 86.7.5 DR Drill Execution
Filename: `86_07_05_dr_drill.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Practice DR procedures

- [ ] Scheduled drills
- [ ] Full failover test
- [ ] RTO/RPO measurement
- [ ] Lessons learned

**Expected Behavior**: DR drills successful

---

# 86.8 Performance Under HA

## Overview
Maintaining performance in HA setup.

## Tasks

### - [ ] 86.8.1 HA Overhead Analysis
Filename: `86_08_01_ha_overhead.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Measure HA performance cost

- [ ] Synchronous replication cost
- [ ] Heartbeat overhead
- [ ] Additional latency
- [ ] Resource consumption

**Expected Behavior**: Overhead understood

---

### - [ ] 86.8.2 Optimizing Replication Lag
Filename: `86_08_02_replication_lag.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Minimize replication delay

- [ ] Lag monitoring
- [ ] Network optimization
- [ ] Synchronous options
- [ ] Acceptable thresholds

**Expected Behavior**: Lag minimized

---

### - [ ] 86.8.3 Health Check Tuning
Filename: `86_08_03_health_check_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize health checks

- [ ] Check frequency
- [ ] Timeout settings
- [ ] False positive reduction
- [ ] Fast detection balance

**Expected Behavior**: Health checks optimal

---

### - [ ] 86.8.4 Failover Time Optimization
Filename: `86_08_04_failover_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Minimize failover time

- [ ] Detection time
- [ ] Promotion time
- [ ] Connection re-establishment
- [ ] End-to-end RTO

**Expected Behavior**: Fast failover

---

### - [ ] 86.8.5 Read Replica Utilization
Filename: `86_08_05_read_replica_usage.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Offload to read replicas

- [ ] Query routing
- [ ] Read-only operations
- [ ] Consistency considerations
- [ ] Performance gains

**Expected Behavior**: Replicas utilized

---

# 86.9 Debugging HA Issues

## Overview
Troubleshooting HA problems.

## Tasks

### - [ ] 86.9.1 Split-Brain Diagnosis
Filename: `86_09_01_split_brain.py` | Tags: `['reference', 'debugging', 'advanced', 'failure']`

**Purpose**: Detect and fix split-brain

- [ ] Split-brain symptoms
- [ ] Detection mechanisms
- [ ] Resolution procedures
- [ ] Prevention strategies

**Expected Behavior**: Split-brain resolved

---

### - [ ] 86.9.2 Failover Failure Analysis
Filename: `86_09_02_failover_failure.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug failed failover

- [ ] Identify blocking issue
- [ ] Quorum problems
- [ ] Network partition
- [ ] Manual intervention

**Expected Behavior**: Failover fixed

---

### - [ ] 86.9.3 Replication Issues
Filename: `86_09_03_replication_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug replication problems

- [ ] Replication stopped
- [ ] Data inconsistency
- [ ] Conflict resolution
- [ ] Re-sync procedures

**Expected Behavior**: Replication restored

---

### - [ ] 86.9.4 Health Check False Positives
Filename: `86_09_04_health_check_false.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug incorrect health signals

- [ ] Flapping detection
- [ ] Timeout tuning
- [ ] Network issues
- [ ] Load-related failures

**Expected Behavior**: False positives fixed

---

### - [ ] 86.9.5 Recovery Procedure Failures
Filename: `86_09_05_recovery_failures.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug recovery issues

- [ ] Stuck recovery
- [ ] Data corruption
- [ ] State inconsistency
- [ ] Manual recovery steps

**Expected Behavior**: Recovery completed

---

# 86.10 Real-World Examples

## Overview
Production HA implementations.

## Tasks

### - [ ] 86.10.1 AWS Production HA Setup
Filename: `86_10_01_aws_ha_setup.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: AWS HA configuration

- [ ] Multi-AZ deployment
- [ ] RDS Multi-AZ
- [ ] EKS node groups
- [ ] ALB health checks

**Expected Behavior**: AWS HA works

---

### - [ ] 86.10.2 GCP Production HA Setup
Filename: `86_10_02_gcp_ha_setup.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: GCP HA configuration

- [ ] Regional GKE
- [ ] Cloud SQL HA
- [ ] Load balancing
- [ ] Managed certificates

**Expected Behavior**: GCP HA works

---

### - [ ] 86.10.3 On-Premises HA Setup
Filename: `86_10_03_on_prem_ha.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: On-prem HA configuration

- [ ] Patroni PostgreSQL
- [ ] HAProxy setup
- [ ] Keepalived VIP
- [ ] Shared storage

**Expected Behavior**: On-prem HA works

---

### - [ ] 86.10.4 Cross-Region Active-Passive
Filename: `86_10_04_cross_region_passive.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: DR site configuration

- [ ] Warm standby setup
- [ ] Data replication
- [ ] Failover procedures
- [ ] DNS switching

**Expected Behavior**: DR site ready

---

### - [ ] 86.10.5 Active-Active Multi-Region
Filename: `86_10_05_active_active.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Active-active setup

- [ ] Regional isolation
- [ ] Data partitioning
- [ ] Global load balancing
- [ ] Conflict avoidance

**Expected Behavior**: Active-active works

---

# Summary

## Topic Completion Checklist
- [ ] Scheduler HA documented
- [ ] Database HA covered
- [ ] Worker HA explained
- [ ] Webserver HA included
- [ ] DR procedures provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 85: Deployment Patterns (deployment basics)
- Section 87: Scaling (scaling for HA)
- Section 93: Health Checks (health monitoring)
- Section 91: Alerting (failure alerts)

## Notes for Implementation
- Include Kubernetes manifests
- Show Patroni configuration
- Demonstrate failover procedures
- Provide monitoring queries

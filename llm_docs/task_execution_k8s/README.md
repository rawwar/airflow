# Task Execution Documentation - KubernetesExecutor

Comprehensive guide to understanding and debugging task execution on KubernetesExecutor, from scheduler queuing to pod completion.

## Quick Links

| Resource | Description |
|----------|-------------|
| **[kubernetes_task_lifecycle.md](kubernetes_task_lifecycle.md)** | Main documentation (1,800+ lines, 15+ diagrams) |
| **[excalidraw/](excalidraw/)** | Editable diagrams (2 files created) |

## What's Inside

### Main Documentation: kubernetes_task_lifecycle.md

**1. Overview**
- KubernetesExecutor fundamentals
- Execution phases (8 phases from queue to cleanup)
- Architecture diagram

**2. Architecture Components**
- KubernetesExecutor, AirflowKubernetesScheduler, K8s API, Task Pods
- task_queue and result_queue (multiprocessing.Queue)
- Component interactions and roles

**3. Complete Execution Flow**
- 8-phase detailed sequence
- Timeline with typical durations (5-35s overhead)
- State transitions and watch mechanism

**4. Pod Creation and Lifecycle**
- Pod generation process
- Pod lifecycle states (Pending → Running → Succeeded/Failed)
- Pod naming convention

**5. Pod Specification**
- Default pod template with YAML
- executor_config customization
- Common customizations (resources, images, node affinity, secrets)

**6. XCom Operations**
- Same as CeleryExecutor behavior
- Key differences (no shared memory, DB-only channel)
- Best practices for pod isolation

**7. Variable Access**
- Variable.get() caching (10,000x faster)
- Kubernetes Secrets alternative (better for K8s)
- Setup and configuration

**8. Database Connections**
- Connection pooling considerations
- Total connections = (active pods) × (pool_size)
- Best practices for high pod counts

**9. Logging and Monitoring**
- Log architecture (local PV, remote S3/GCS, kubectl logs)
- Remote logging REQUIRED for production
- Pod lifecycle and log retention
- Metrics (StatsD, Prometheus)

**10. Pod Watching and State Sync**
- Watch mechanism (streaming API)
- Resource version tracking
- Event processing and pod adoption

**11. Resource Management**
- Requests vs Limits
- Pod lifecycle configuration
- Multi-namespace mode
- Resource quotas and handling

**12. Debugging Guide**
- 5 common issues with solutions:
  1. Task stuck in QUEUED (RBAC, API, quota)
  2. Pod stuck in Pending (resources, image, node selector)
  3. Pod fails with OOMKilled (memory limits)
  4. Logs not available (remote logging)
  5. Image pull errors (credentials, registry)
- Debugging tools (kubectl, SQL queries, K8s events)
- Performance optimization

### Excalidraw Diagrams

**01_complete_flow.excalidraw**  
End-to-end execution with timeline (scheduler → queue → K8sScheduler → API → pod → DB)

**02_pod_lifecycle.excalidraw**  
Pod state machine (Pending → Running → Succeeded/Failed) with timing info

## Quick Reference

### Essential Commands

```bash
# List Airflow worker pods
kubectl get pods -n airflow -l airflow-worker=true

# Describe pod
kubectl describe pod <pod-name> -n airflow

# Get pod logs
kubectl logs <pod-name> -n airflow -f

# Exec into running pod
kubectl exec -it <pod-name> -n airflow -- /bin/bash

# Check events
kubectl get events -n airflow --sort-by='.lastTimestamp'

# Resource usage
kubectl top pods -n airflow
kubectl top nodes

# Airflow commands
airflow tasks test my_dag my_task 2024-01-01
airflow config get-value kubernetes_executor namespace
```

### Key Configuration

```ini
[kubernetes_executor]
namespace = airflow
worker_container_repository = apache/airflow
worker_container_tag = 2.7.3
parallelism = 32
worker_pods_creation_batch_size = 10
delete_worker_pods = True
delete_worker_pods_on_failure = False
```

### Key Files

| Component | File | Key Methods |
|-----------|------|-------------|
| **KubernetesExecutor** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor.py` | `execute_async()`, `sync()`, `adopt_launched_task()` |
| **AirflowKubernetesScheduler** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor_utils.py` | `run_next()`, `sync()`, `_watch_pods()` |
| **PodGenerator** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/pod_generator.py` | `construct_pod()`, `reconcile_pods()` |

### Debugging Checklist

**Task stuck in QUEUED?**
- ☑️ Executor running?
- ☑️ K8s API accessible?
- ☑️ RBAC permissions correct?
- ☑️ Namespace exists?
- ☑️ Resource quota not exceeded?

**Pod stuck in Pending?**
- ☑️ Check `kubectl describe pod`
- ☑️ Sufficient cluster resources?
- ☑️ Image exists and pullable?
- ☑️ Node selector correct?
- ☑️ PVC bound?

**Pod failed?**
- ☑️ Check exit code
- ☑️ Check `kubectl logs`
- ☑️ Check K8s events
- ☑️ OOMKilled? Increase memory
- ☑️ Image pull error? Check credentials

## Key Differences from CeleryExecutor

| Aspect | CeleryExecutor | KubernetesExecutor |
|--------|----------------|--------------------|
| **Isolation** | Process-level | Container/Pod-level |
| **Scalability** | 100s of tasks | 1000s of tasks |
| **Startup Time** | 1-5s | 5-30s |
| **Resource Management** | Fixed worker pool | Dynamic per-task |
| **Dependencies** | Broker (Redis/RabbitMQ) | Kubernetes Cluster |
| **Log Persistence** | Shared volume or remote | Remote logging REQUIRED |
| **Cleanup** | Persistent workers | Ephemeral pods |
| **Customization** | Worker-level | Per-task (executor_config) |

## Related Documentation

- **CeleryExecutor**: `../task_execution/` - For comparison
- **Scheduler**: `../scheduler/` - How DAG runs are created
- **DAG Run Lifecycle**: `../dag_run_lifecycle/` - States and executors comparison
- **Airflow Docs**: https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/

## How to Use This Documentation

**For understanding flow**:
1. Start with main doc Overview section
2. Follow Complete Execution Flow
3. View excalidraw diagrams for visual understanding
4. Compare with CeleryExecutor documentation

**For debugging issues**:
1. Go directly to Debugging Guide section
2. Find your issue in the 5 common scenarios
3. Use debugging checklist
4. Run suggested kubectl commands

**For optimizing performance**:
1. Read Resource Management section
2. Review Pod Specification customization
3. Check Performance Optimization tips
4. Right-size resource requests/limits

---

**Version**: 1.0  
**Last updated**: 2024  
**For**: Apache Airflow with KubernetesExecutor

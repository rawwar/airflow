# Executors Comparison - Task Execution Across Different Backends

This document compares how different executors handle task execution in Apache Airflow, from queuing to completion.

## Table of Contents

1. [Executor Overview](#executor-overview)
2. [LocalExecutor](#localexecutor)
3. [CeleryExecutor](#celeryexecutor)
4. [KubernetesExecutor](#kubernetesexecutor)
5. [Comparison Matrix](#comparison-matrix)
6. [Selection Guide](#selection-guide)

---

## Executor Overview

Executors are responsible for running Airflow tasks. They receive task instances from the scheduler and execute them on workers.

### Common Architecture

```mermaid
flowchart TB
    Scheduler[Scheduler] -->|queue_task_instance| Executor[Executor]
    Executor -->|heartbeat/sync| Scheduler
    Executor -->|dispatch| Workers[Workers]
    Workers -->|update status| DB[(Database)]
    DB -->|query status| Scheduler
    
    style Scheduler fill:#4ecdc4
    style Executor fill:#ffd93d
    style Workers fill:#95e1d3
    style DB fill:#ffec99
```

### Base Executor Interface

**File**: `airflow-core/src/airflow/executors/base_executor.py`

```python
class BaseExecutor:
    def queue_task_instance(self, task_instance, ...) -> None:
        """Queue a task for execution."""
        
    def heartbeat(self) -> None:
        """Sync executor state, trigger tasks."""
        
    def sync(self) -> None:
        """Return completed tasks to scheduler."""
        
    def execute_async(self, key, command, ...) -> None:
        """Execute task asynchronously."""
```

---

## LocalExecutor

**File**: `airflow-core/src/airflow/executors/local_executor.py`

### Architecture

LocalExecutor runs tasks in parallel using Python's `multiprocessing` library on a single machine.

```mermaid
flowchart TB
    subgraph Single Machine
        Scheduler[Scheduler Process]
        
        subgraph LocalExecutor
            Queue[multiprocessing.Queue]
            Manager[Executor Manager]
        end
        
        subgraph Worker Pool
            W1[Worker 1<br/>subprocess]
            W2[Worker 2<br/>subprocess]
            W3[Worker 3<br/>subprocess]
            WN[Worker N<br/>subprocess]
        end
        
        Scheduler -->|queue_task_instance| Manager
        Manager -->|put task| Queue
        Queue -->|get task| W1
        Queue -->|get task| W2
        Queue -->|get task| W3
        Queue -->|get task| WN
        
        W1 -->|update DB| DB[(Database)]
        W2 -->|update DB| DB
        W3 -->|update DB| DB
        WN -->|update DB| DB
        
        DB -->|poll status| Manager
        Manager -->|sync| Scheduler
    end
    
    style Scheduler fill:#4ecdc4
    style Manager fill:#ffd93d
    style Queue fill:#ffec99
    style W1 fill:#95e1d3
    style W2 fill:#95e1d3
    style W3 fill:#95e1d3
    style WN fill:#95e1d3
    style DB fill:#ffd93d
```

### Key Characteristics

**Advantages**:
- Simple setup (no external dependencies)
- Low latency (no network overhead)
- Good for development and small deployments
- Shared filesystem access

**Limitations**:
- Limited to single machine capacity (~32 parallel tasks)
- No high availability (single point of failure)
- Scaling limited by machine resources

**Use Cases**:
- Development environments
- Testing
- Small production workloads (<50 DAGs)


---

## CeleryExecutor

**File**: `providers/celery/src/airflow/providers/celery/executors/celery_executor.py`

### Architecture

CeleryExecutor distributes tasks across multiple worker machines using a message broker (Redis/RabbitMQ).

```mermaid
flowchart TB
    subgraph Scheduler Machine
        Scheduler[Scheduler Process]
        CeleryExec[CeleryExecutor]
    end
    
    subgraph Message Infrastructure
        Broker[(Message Broker<br/>Redis/RabbitMQ)]
        Backend[(Result Backend<br/>Redis/Database)]
    end
    
    subgraph Worker Machine 1
        CW1[Celery Worker 1]
        T1[Task Processes]
    end
    
    subgraph Worker Machine N
        CWN[Celery Worker N]
        TN[Task Processes]
    end
    
    Scheduler -->|queue_task_instance| CeleryExec
    CeleryExec -->|apply_async| Broker
    Broker -->|dispatch| CW1
    Broker -->|dispatch| CWN
    CW1 -->|spawn| T1
    CWN -->|spawn| TN
    T1 -->|write result| Backend
    TN -->|write result| Backend
    Backend -->|poll results| CeleryExec
    CeleryExec -->|sync| Scheduler
    T1 -.->|update state| DB[(Metadata DB)]
    TN -.->|update state| DB
    
    style Scheduler fill:#4ecdc4
    style CeleryExec fill:#ffd93d
    style Broker fill:#f08c00,color:#fff
    style Backend fill:#f08c00,color:#fff
    style CW1 fill:#95e1d3
    style CWN fill:#95e1d3
    style T1 fill:#b2f2bb
    style TN fill:#b2f2bb
    style DB fill:#ffd93d
```

### Key Characteristics

**Advantages**:
- Horizontal scalability (add more worker machines)
- High availability (multiple workers)
- Queue-based routing (priority, resource-specific)
- Battle-tested (Celery is mature)

**Limitations**:
- Requires broker infrastructure (Redis/RabbitMQ)
- More complex setup and monitoring
- Network latency between components

**Use Cases**:
- Medium to large production deployments (50-1000 DAGs)
- Need for high availability
- Heterogeneous worker pools (CPU/GPU optimized)

---

## KubernetesExecutor

**File**: `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor.py`

### Architecture

KubernetesExecutor creates a new pod for each task, providing complete isolation.

```mermaid
flowchart TB
    subgraph Airflow Scheduler Pod
        Scheduler[Scheduler Process]
        K8sExec[KubernetesExecutor]
    end
    
    subgraph Kubernetes Cluster
        API[Kubernetes API Server]
        
        subgraph Worker Pods
            P1[Pod: task-123<br/>Running]
            P2[Pod: task-456<br/>Running]
            P3[Pod: task-789<br/>Succeeded]
        end
        
        PV[(Persistent Volume<br/>DAGs/Logs)]
    end
    
    Scheduler -->|queue_task_instance| K8sExec
    K8sExec -->|create_pod| API
    API -->|schedule| P1
    API -->|schedule| P2
    API -->|schedule| P3
    K8sExec -->|watch| API
    P1 -.->|mount| PV
    P2 -.->|mount| PV
    P3 -.->|mount| PV
    P1 -->|update state| DB[(Metadata DB)]
    P2 -->|update state| DB
    P3 -->|update state| DB
    K8sExec -->|sync| Scheduler
    
    style Scheduler fill:#4ecdc4
    style K8sExec fill:#ffd93d
    style API fill:#f08c00,color:#fff
    style P1 fill:#95e1d3
    style P2 fill:#95e1d3
    style P3 fill:#b2f2bb
    style PV fill:#ffec99
    style DB fill:#ffd93d
```

### Pod Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Pending: Executor creates pod
    Pending --> Running: Kubernetes schedules pod
    Running --> Succeeded: Task completes successfully
    Running --> Failed: Task fails
    Succeeded --> Deleted: Cleanup
    Failed --> Deleted: Cleanup
    Deleted --> [*]
    
    note right of Pending
        Pod created via K8s API
        Waiting for resources
    end note
    
    note right of Running
        Container executing
        airflow tasks run command
    end note
```

### Key Characteristics

**Advantages**:
- Complete isolation (each task in separate pod)
- Massive scalability (limited only by K8s cluster)
- Resource efficiency (pods created/destroyed on demand)
- Custom environments (per-task images, resources)

**Limitations**:
- Higher startup latency (pod creation + image pull)
- Requires Kubernetes cluster
- More complex troubleshooting

**Use Cases**:
- Cloud-native deployments
- Large-scale production (1000+ DAGs)
- Tasks requiring different environments
- Need for strong task isolation

---

## Comparison Matrix

| Feature | LocalExecutor | CeleryExecutor | KubernetesExecutor |
|---------|---------------|----------------|--------------------|
| **Deployment Complexity** | Low | Medium | High |
| **External Dependencies** | None | Broker + Backend | Kubernetes Cluster |
| **Scalability** | Vertical | Horizontal | Horizontal |
| **Parallel Tasks** | ~32 | 100s-1000s | 1000s-10000s |
| **Task Isolation** | Process-level | Process-level | Container-level |
| **Startup Latency** | Low (<1s) | Low-Medium (1-5s) | Medium-High (5-30s) |
| **High Availability** | No | Yes | Yes |
| **Best For** | Dev/small | Production/medium | Cloud/large |

---

## Selection Guide

### Decision Flowchart

```mermaid
flowchart TD
    Start([Choose Executor]) --> Q1{Development or<br/>Production?}
    Q1 -->|Development| Local[LocalExecutor]
    Q1 -->|Production| Q2{Expected scale?}
    Q2 -->|<50 DAGs| Local
    Q2 -->|50-500 DAGs| Q3{Have Kubernetes?}
    Q2 -->|>500 DAGs| K8s[KubernetesExecutor]
    Q3 -->|Yes| K8s
    Q3 -->|No| Celery[CeleryExecutor]
    
    style Start fill:#4ecdc4
    style Local fill:#ffec99
    style Celery fill:#95e1d3
    style K8s fill:#b2f2bb
```

### Recommendations by Use Case

| Use Case | Recommended Executor | Rationale |
|----------|---------------------|----------|
| Local development | LocalExecutor | Simple, no dependencies |
| Small production | LocalExecutor | Cost-effective |
| Medium production | CeleryExecutor | Good balance |
| Large production | KubernetesExecutor | Scalability, isolation |
| Cloud-native | KubernetesExecutor | Native K8s integration |

**Next Steps**: See `lifecycle_overview.md` for complete DAG run flow and `state_machines.md` for state transitions.

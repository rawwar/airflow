# Task Execution Lifecycle on KubernetesExecutor - Complete Guide

Comprehensive documentation for debugging and understanding task execution on KubernetesExecutor, from scheduler queuing to pod completion.

## Table of Contents

1. [Overview](#overview)
2. [Architecture Components](#architecture-components)
3. [Complete Execution Flow](#complete-execution-flow)
4. [Pod Creation and Lifecycle](#pod-creation-and-lifecycle)
5. [Pod Specification](#pod-specification)
6. [XCom Operations](#xcom-operations)
7. [Variable Access](#variable-access)
8. [Database Connections](#database-connections)
9. [Logging and Monitoring](#logging-and-monitoring)
10. [Pod Watching and State Sync](#pod-watching-and-state-sync)
11. [Resource Management](#resource-management)
12. [Debugging Guide](#debugging-guide)

---

## Overview

### What is KubernetesExecutor?

KubernetesExecutor creates a new Kubernetes pod for each task, providing complete isolation and massive scalability.

**Key Characteristics**:
- Each task runs in its own pod
- Pods created on-demand and cleaned up after completion
- Full Kubernetes API support for customization
- Native cloud integration

### Execution Phases

```mermaid
flowchart TB
    subgraph Phase 1: Scheduler
        S1[Scheduler: queue_task_instance]
        S2[Build KubernetesJob]
        S3[Put in task_queue]
    end
    
    subgraph Phase 2: Executor Sync
        E1[executor.sync called]
        E2[Process task_queue]
        E3[kube_scheduler.run_next]
    end
    
    subgraph Phase 3: Pod Creation
        P1[Generate pod spec]
        P2[Apply executor_config]
        P3[Call K8s API create_namespaced_pod]
    end
    
    subgraph Phase 4: Kubernetes Scheduling
        K1[K8s scheduler assigns node]
        K2[Pull container image]
        K3[Pod transitions Pending->Running]
    end
    
    subgraph Phase 5: Task Execution
        T1[Container starts]
        T2[airflow tasks run command]
        T3[Load DAG and execute]
        T4[Access DB for XCom/Variables]
    end
    
    subgraph Phase 6: Pod Completion
        C1[Task completes]
        C2[Container exits with code]
        C3[Pod state: Succeeded/Failed]
    end
    
    subgraph Phase 7: State Sync
        W1[Watcher detects pod event]
        W2[Put result in result_queue]
        W3[executor.sync processes result]
        W4[Update TaskInstance state]
    end
    
    subgraph Phase 8: Cleanup
        CL1[Pod marked for deletion]
        CL2[Logs persisted]
        CL3[Pod removed from K8s]
    end
    
    S1 --> S2 --> S3
    S3 --> E1 --> E2 --> E3
    E3 --> P1 --> P2 --> P3
    P3 --> K1 --> K2 --> K3
    K3 --> T1 --> T2 --> T3 --> T4
    T4 --> C1 --> C2 --> C3
    C3 --> W1 --> W2 --> W3 --> W4
    W4 --> CL1 --> CL2 --> CL3
    
    style S1 fill:#4ecdc4
    style E1 fill:#ffd93d
    style P1 fill:#ffec99
    style K1 fill:#f08c00,color:#fff
    style T1 fill:#95e1d3
    style C3 fill:#b2f2bb
    style W1 fill:#d0ebff
    style CL1 fill:#868e96
```

---

## Architecture Components

### Component Diagram

```mermaid
flowchart TB
    subgraph Scheduler Pod
        Scheduler[Scheduler Process]
        KubeExec[KubernetesExecutor]
        TaskQueue[task_queue<br/>multiprocessing.Queue]
        ResultQueue[result_queue<br/>multiprocessing.Queue]
        KubeScheduler[AirflowKubernetesScheduler<br/>separate process]
    end
    
    subgraph Kubernetes Cluster
        APIServer[K8s API Server]
        
        subgraph Worker Pods
            Pod1[Task Pod 1<br/>dag_id.task_id.try]
            Pod2[Task Pod 2]
            Pod3[Task Pod 3]
        end
        
        subgraph Storage
            PV[(Persistent Volume<br/>for DAGs/logs)]
        end
    end
    
    subgraph External
        DB[(Metadata DB)]
        Logs[Remote Logs<br/>S3/GCS]
    end
    
    Scheduler -->|execute_async| KubeExec
    KubeExec -->|put KubernetesJob| TaskQueue
    TaskQueue -->|get_nowait| KubeScheduler
    KubeScheduler -->|create_namespaced_pod| APIServer
    APIServer -->|schedule| Pod1
    APIServer -->|schedule| Pod2
    APIServer -->|schedule| Pod3
    KubeScheduler -.->|watch pods| APIServer
    APIServer -.->|pod events| KubeScheduler
    KubeScheduler -->|put results| ResultQueue
    ResultQueue -->|get_nowait| KubeExec
    KubeExec -->|_change_state| Scheduler
    Pod1 -->|mount| PV
    Pod2 -->|mount| PV
    Pod3 -->|mount| PV
    Pod1 -->|query/update| DB
    Pod2 -->|query/update| DB
    Pod3 -->|query/update| DB
    Pod1 -.->|upload| Logs
    Pod2 -.->|upload| Logs
    Pod3 -.->|upload| Logs
    
    style Scheduler fill:#4ecdc4
    style KubeExec fill:#ffd93d
    style TaskQueue fill:#ffec99
    style ResultQueue fill:#ffec99
    style KubeScheduler fill:#95e1d3
    style APIServer fill:#f08c00,color:#fff
    style Pod1 fill:#b2f2bb
    style Pod2 fill:#b2f2bb
    style Pod3 fill:#b2f2bb
    style DB fill:#ffd93d
    style PV fill:#ffec99
```

### Component Roles

**KubernetesExecutor** (`kubernetes_executor.py`):
- Receives tasks from scheduler via `execute_async()`
- Queues tasks into `task_queue` (multiprocessing.Queue)
- Processes results from `result_queue`
- Updates task states via `_change_state()`
- Manages `queued_tasks`, `running`, and `completed` sets

**AirflowKubernetesScheduler** (`kubernetes_executor_utils.py`):
- Runs in separate process (forked from executor)
- Pulls tasks from `task_queue`
- Generates pod specifications
- Calls Kubernetes API to create pods
- Watches pods for status changes
- Puts results into `result_queue`

**Kubernetes API Server**:
- Receives pod creation requests
- Schedules pods onto worker nodes
- Manages pod lifecycle
- Provides watch API for pod events

**Task Pods**:
- Ephemeral pods created per task
- Run `airflow tasks run` command
- Access metadata DB for state/XCom/variables
- Mount DAG files from persistent volume
- Upload logs to remote storage (optional)

---

## Complete Execution Flow

### Detailed Sequence Diagram

```mermaid
sequenceDiagram
    participant Sch as Scheduler
    participant Exec as KubernetesExecutor
    participant TQ as task_queue
    participant KS as KubeScheduler Process
    participant API as K8s API
    participant Pod as Task Pod
    participant DB as Metadata DB
    participant RQ as result_queue
    
    Note over Sch: Task ready to run
    Sch->>Exec: execute_async(key, command, config)
    Exec->>Exec: Build KubernetesJob
    Exec->>TQ: put(job)
    Exec->>Exec: event_buffer[key] = QUEUED
    
    Note over Sch: Scheduler loop continues
    Sch->>Exec: sync()
    Exec->>RQ: check for completed tasks
    Exec->>TQ: get_nowait() up to batch_size
    TQ->>Exec: KubernetesJob
    Exec->>KS: run_next(job)
    
    Note over KS: Generate pod spec
    KS->>KS: PodGenerator.construct_pod()
    KS->>KS: Apply executor_config
    KS->>KS: Add labels & annotations
    KS->>API: create_namespaced_pod(pod_spec)
    API->>KS: 201 Created
    
    Note over API: K8s scheduler assigns node
    API->>API: Schedule pod to node
    API->>API: Pull image (if needed)
    API->>Pod: Start container
    
    Note over Pod: Task execution begins
    Pod->>Pod: airflow tasks run dag_id task_id date
    Pod->>DB: Load TaskInstance
    Pod->>DB: Query XCom/Variables
    Pod->>Pod: Execute operator logic
    Pod->>DB: Push XCom (if any)
    Pod->>DB: Update state to SUCCESS/FAILED
    Pod->>Pod: Exit with code 0 or 1
    
    Note over API: Pod completes
    API->>API: Pod state: Succeeded/Failed
    
    Note over KS: Watcher detects event
    KS->>API: watch pods (streaming)
    API-->>KS: Pod event: phase=Succeeded
    KS->>KS: Process pod event
    KS->>RQ: put(KubernetesResults)
    
    Note over Sch: Next scheduler sync
    Sch->>Exec: sync()
    Exec->>RQ: get_nowait()
    RQ->>Exec: KubernetesResults
    Exec->>Exec: _change_state(results)
    Exec->>Sch: success(key) or fail(key)
    
    Note over API: Cleanup
    API->>API: Delete pod (after grace period)
```

### Execution Timeline

```mermaid
gantt
    title Task Execution Timeline (Typical Durations)
    dateFormat X
    axisFormat %Ss
    
    section Queueing
    execute_async         :0, 10ms
    In task_queue          :10ms, 100ms
    
    section Pod Creation
    sync() processes queue :100ms, 200ms
    Generate pod spec      :200ms, 300ms
    K8s API call           :300ms, 500ms
    
    section Scheduling
    K8s assigns node       :500ms, 1s
    Pull image (cached)    :1s, 2s
    Pull image (uncached)  :1s, 60s
    Start container        :2s, 3s
    
    section Execution
    Task runs              :3s, 33s
    
    section Completion
    Pod exits              :33s, 33.1s
    Watcher detects event  :33.1s, 33.5s
    Result in result_queue :33.5s, 34s
    sync() processes result:34s, 35s
```

**Key Timing Notes**:
- **Image pull**: Biggest variable (0-60s depending on cache)
- **Pod startup**: 2-5s typical
- **Total overhead**: 5-30s (vs 1-5s for CeleryExecutor)
- **Parallelism**: Limited by K8s cluster capacity (1000s+)

---

## Pod Creation and Lifecycle

### Pod Generation Process

```mermaid
flowchart TD
    Start([run_next called]) --> GetBase[Get base pod template]
    GetBase --> Source{Pod template<br/>source?}
    
    Source -->|pod_template_file| LoadFile[Load YAML file]
    Source -->|pod_override| UseOverride[Use executor_config]
    Source -->|Default| UseDefault[Use kube_config defaults]
    
    LoadFile --> Merge
    UseOverride --> Merge
    UseDefault --> Merge
    
    Merge[Merge configurations] --> AddLabels[Add Airflow labels]
    AddLabels --> AddAnnotations[Add annotations]
    AddAnnotations --> AddEnv[Add environment vars]
    AddEnv --> AddVolumes[Add volumes/mounts]
    AddVolumes --> AddResources[Add resource requests/limits]
    AddResources --> SetCommand[Set command args]
    SetCommand --> Hook{Pod mutation<br/>hook?}
    
    Hook -->|Yes| CallHook[Call hook function]
    Hook -->|No| Validate
    CallHook --> Validate[Validate pod spec]
    
    Validate --> Create[Call K8s API]
    Create --> Done([Pod created])
    
    style Start fill:#4ecdc4
    style Merge fill:#ffd93d
    style Validate fill:#ffec99
    style Create fill:#f08c00,color:#fff
    style Done fill:#b2f2bb
```

### Pod Lifecycle States

```mermaid
stateDiagram-v2
    [*] --> Pending: API creates pod
    
    Pending --> Running: Container starts
    Pending --> Failed: Image pull error
    Pending --> Failed: Invalid spec
    
    Running --> Succeeded: Exit code 0
    Running --> Failed: Exit code != 0
    Running --> Failed: OOMKilled
    Running --> Failed: Node failure
    
    Succeeded --> Succeeded: Grace period
    Failed --> Failed: Grace period
    
    Succeeded --> [*]: Pod deleted
    Failed --> [*]: Pod deleted
    
    note right of Pending
        Waiting for:
        - Node assignment
        - Image pull
        - Volume mounts
    end note
    
    note right of Running
        Container executing
        airflow tasks run
        command
    end note
    
    note right of Succeeded
        Task completed
        Exit code 0
        Logs available
    end note
    
    note right of Failed
        Task failed
        Check:
        - Exit code
        - Logs
        - K8s events
    end note
```

### Pod Naming Convention

**Format**: `{dag_id}-{task_id}-{unique_suffix}`

**Example**: `my_dag-extract_data-a1b2c3d4`

**Rules**:
- Max 63 characters (DNS-1123 label)
- Lowercase alphanumeric + hyphens
- Unique suffix ensures no collisions
- Logical date NOT in name (in labels)

---

## Pod Specification

### Default Pod Template

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: airflow-worker-{unique}
  namespace: airflow
  labels:
    airflow-worker: "true"
    dag_id: "{{ dag_id }}"
    task_id: "{{ task_id }}"
    try_number: "{{ try_number }}"
    airflow_version: "{{ airflow_version }}"
  annotations:
    dag_id: "{{ dag_id }}"
    task_id: "{{ task_id }}"
    logical_date: "{{ logical_date_iso }}"
spec:
  restartPolicy: Never
  serviceAccountName: airflow-worker
  containers:
  - name: base
    image: apache/airflow:2.x
    command:
      - airflow
      - tasks
      - run
      - "{{ dag_id }}"
      - "{{ task_id }}"
      - "{{ logical_date }}"
      - --local
      - --subdir
      - "{{ dag_folder }}"
    env:
      - name: AIRFLOW__CORE__EXECUTOR
        value: LocalExecutor
      - name: AIRFLOW__DATABASE__SQL_ALCHEMY_CONN
        valueFrom:
          secretKeyRef:
            name: airflow-secrets
            key: sql_alchemy_conn
    volumeMounts:
      - name: dags
        mountPath: /opt/airflow/dags
        readOnly: true
      - name: logs
        mountPath: /opt/airflow/logs
    resources:
      requests:
        memory: "512Mi"
        cpu: "0.5"
      limits:
        memory: "1Gi"
        cpu: "1"
  volumes:
    - name: dags
      persistentVolumeClaim:
        claimName: airflow-dags
    - name: logs
      persistentVolumeClaim:
        claimName: airflow-logs
```

### Executor Config Customization

**In DAG file**:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from kubernetes.client import models as k8s

my_task = PythonOperator(
    task_id='memory_intensive_task',
    python_callable=my_function,
    executor_config={
        "pod_override": k8s.V1Pod(
            spec=k8s.V1PodSpec(
                containers=[
                    k8s.V1Container(
                        name="base",
                        resources=k8s.V1ResourceRequirements(
                            requests={"memory": "4Gi", "cpu": "2"},
                            limits={"memory": "8Gi", "cpu": "4"},
                        ),
                        env=[
                            k8s.V1EnvVar(
                                name="MY_ENV_VAR",
                                value="custom_value"
                            )
                        ],
                    )
                ],
                node_selector={"workload": "memory-optimized"},
                tolerations=[
                    k8s.V1Toleration(
                        key="dedicated",
                        operator="Equal",
                        value="airflow",
                        effect="NoSchedule"
                    )
                ],
            )
        ),
        "pod_template_file": "/path/to/custom_template.yaml",
    },
)
```

### Common Customizations

**1. Resource Limits**
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            containers=[k8s.V1Container(
                name="base",
                resources=k8s.V1ResourceRequirements(
                    requests={"memory": "2Gi", "cpu": "1"},
                    limits={"memory": "4Gi", "cpu": "2"},
                )
            )]
        )
    )
}
```

**2. Custom Image**
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            containers=[k8s.V1Container(
                name="base",
                image="my-registry.com/airflow:custom-v1.0",
                image_pull_policy="Always",
            )]
        )
    )
}
```

**3. Node Affinity**
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            affinity=k8s.V1Affinity(
                node_affinity=k8s.V1NodeAffinity(
                    required_during_scheduling_ignored_during_execution=
                        k8s.V1NodeSelector(
                            node_selector_terms=[k8s.V1NodeSelectorTerm(
                                match_expressions=[k8s.V1NodeSelectorRequirement(
                                    key="node.kubernetes.io/instance-type",
                                    operator="In",
                                    values=["c5.2xlarge", "c5.4xlarge"]
                                )]
                            )]
                        )
                )
            )
        )
    )
}
```

**4. Secrets and ConfigMaps**
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            containers=[k8s.V1Container(
                name="base",
                env_from=[
                    k8s.V1EnvFromSource(
                        secret_ref=k8s.V1SecretEnvSource(
                            name="my-task-secrets"
                        )
                    ),
                    k8s.V1EnvFromSource(
                        config_map_ref=k8s.V1ConfigMapEnvSource(
                            name="my-task-config"
                        )
                    )
                ]
            )]
        )
    )
}
```

---

## XCom Operations

### XCom in Kubernetes Pods

**Same as CeleryExecutor** - XCom operations work identically:

```mermaid
flowchart LR
    subgraph Pod 1
        T1[Task 1: Producer]
    end
    
    subgraph Metadata DB
        XComTable[(xcom table)]
    end
    
    subgraph Pod 2
        T2[Task 2: Consumer]
    end
    
    T1 -->|ti.xcom_push| XComTable
    XComTable -->|ti.xcom_pull| T2
    
    style T1 fill:#4ecdc4
    style XComTable fill:#ffd93d
    style T2 fill:#95e1d3
```

**Key Differences from Celery**:
1. **No shared memory** - Each pod is isolated
2. **DB is only channel** - Must use metadata DB for XCom
3. **Network overhead** - Pod-to-DB network latency

**Best Practices**:
- Keep XCom values < 1 MB
- Use JSON serialization (default)
- For large data, use S3/GCS with XCom storing only URIs
- Consider using TaskFlow API for cleaner XCom handling

**Example**:
```python
@task
def extract() -> dict:
    return {"data": "value"}  # Automatically pushed to XCom

@task
def transform(data: dict) -> dict:  # Automatically pulled from XCom
    return {"result": data["data"].upper()}

@dag(...)
def my_dag():
    transform(extract())
```

---

## Variable Access

### Variable.get() in Pods

**Behavior**: Same caching mechanism as CeleryExecutor

```python
from airflow.models import Variable

# First call: DB query (~10ms)
api_key = Variable.get("api_key")

# Subsequent calls in same task: Cache hit (~1µs)
for i in range(1000):
    key = Variable.get("api_key")  # Instant!
```

**Cache Scope**: Task execution lifetime (pod lifetime)

**Important**: Cache cleared between task retries (new pod)

### Kubernetes Secrets Alternative

**Better approach for secrets in K8s**:

```python
import os

# Instead of Variable.get(), use K8s secrets
api_key = os.getenv("API_KEY")  # Injected from K8s secret
```

**Advantages**:
- No DB query overhead
- Native K8s secret management
- Automatic rotation support
- Better security (secrets not in Airflow DB)

**Setup**:

1. Create K8s secret:
```bash
kubectl create secret generic api-secrets   --from-literal=api_key=secret123
```

2. Use in executor_config:
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            containers=[k8s.V1Container(
                name="base",
                env=[
                    k8s.V1EnvVar(
                        name="API_KEY",
                        value_from=k8s.V1EnvVarSource(
                            secret_key_ref=k8s.V1SecretKeySelector(
                                name="api-secrets",
                                key="api_key"
                            )
                        )
                    )
                ]
            )]
        )
    )
}
```

---

## Database Connections

### Connection Pooling

**Challenge**: Each pod is independent

**Configuration**:
```ini
[database]
sql_alchemy_pool_size = 5        # Per-pod pool size
sql_alchemy_max_overflow = 10
sql_alchemy_pool_pre_ping = True  # Detect stale connections
sql_alchemy_pool_recycle = 3600   # Recycle after 1 hour
```

**Considerations**:
- **Total connections** = `(active pods) × (pool_size + max_overflow)`
- With 100 pods: 100 × 15 = 1,500 DB connections
- DB must support this connection count
- Use connection pooler (PgBouncer) for Postgres

### Connection String

**Injected via environment variable**:
```yaml
env:
  - name: AIRFLOW__DATABASE__SQL_ALCHEMY_CONN
    valueFrom:
      secretKeyRef:
        name: airflow-secrets
        key: sql_alchemy_conn
```

**Value format**:
```
postgresql+psycopg2://user:pass@postgres-svc.airflow.svc.cluster.local:5432/airflow
```

**Best Practices**:
1. Use K8s Service DNS for DB (not external IP)
2. Enable `pool_pre_ping` to handle connection resets
3. Set `pool_recycle` to handle DB-side timeouts
4. Monitor DB connection count with metrics

---

## Logging and Monitoring

### Log Architecture

```mermaid
flowchart TB
    subgraph Task Pod
        Task[Task Execution]
        Stdout[stdout/stderr]
        Handler[Log Handler]
    end
    
    subgraph Storage Options
        Local[Local PV<br/>/opt/airflow/logs]
        S3[S3 Bucket<br/>s3://bucket/logs]
        GCS[GCS Bucket<br/>gs://bucket/logs]
        Azure[Azure Blob<br/>wasb://container]
    end
    
    subgraph Kubernetes
        KubeLogs[kubectl logs]
    end
    
    Task --> Stdout
    Stdout --> Handler
    Handler -->|write| Local
    Handler -->|upload| S3
    Handler -->|upload| GCS
    Handler -->|upload| Azure
    Stdout -.->|captured| KubeLogs
    
    style Task fill:#4ecdc4
    style Handler fill:#ffd93d
    style Local fill:#ffec99
    style S3 fill:#95e1d3
    style GCS fill:#95e1d3
    style Azure fill:#95e1d3
```

### Log Configuration

**Local logs** (default):
```ini
[logging]
base_log_folder = /opt/airflow/logs
remote_logging = False
```

**Remote logs** (S3 example):
```ini
[logging]
remote_logging = True
remote_base_log_folder = s3://my-bucket/airflow-logs
remote_log_conn_id = aws_default

[aws]
conn_type = aws
aws_access_key_id = AKIA...
aws_secret_access_key = ...
region_name = us-east-1
```

**GCS example**:
```ini
[logging]
remote_logging = True
remote_base_log_folder = gs://my-bucket/airflow-logs
remote_log_conn_id = google_cloud_default
```

### Log Lifecycle

```mermaid
sequenceDiagram
    participant Pod
    participant Local as Local Volume
    participant Remote as Remote Storage
    participant UI as Airflow UI
    
    Pod->>Local: Write logs during execution
    Pod->>Pod: Task completes
    Pod->>Remote: Upload logs (if configured)
    Note over Pod: Pod deletion
    Pod->>Pod: Grace period (30s)
    Pod->>Pod: Terminated
    
    Note over UI: User views logs
    UI->>Remote: Fetch from S3/GCS
    Remote->>UI: Return log file
    
    alt Logs not in remote
        UI->>Local: Try local volume
        Local->>UI: Return if still available
    end
    
    alt No logs found
        UI->>UI: Show "Log not found"
    end
```

**Important**: 
- Without remote logging, logs lost when pod deleted
- Local volume only works if pod still exists
- Remote logging REQUIRED for production

### kubectl logs

**View live logs**:
```bash
# Find pod name
kubectl get pods -n airflow -l dag_id=my_dag,task_id=my_task

# View logs
kubectl logs -n airflow <pod-name> -f

# Previous pod (if restarted)
kubectl logs -n airflow <pod-name> --previous
```

**Limitations**:
- Only available while pod exists
- Lost after pod deletion
- Not accessible from Airflow UI

### Metrics

**StatsD metrics** (same as CeleryExecutor):
```python
from airflow.stats import Stats

Stats.incr('my_dag.my_task.success')
Stats.timing('my_dag.my_task.duration', duration_ms)
Stats.gauge('my_dag.my_task.records_processed', count)
```

**Kubernetes-specific metrics**:
- Pod creation time
- Image pull duration
- Pod scheduling latency
- Resource usage per pod

**Prometheus example**:
```yaml
apiVersion: v1
kind: ServiceMonitor
metadata:
  name: airflow-worker-pods
spec:
  selector:
    matchLabels:
      airflow-worker: "true"
  endpoints:
  - port: metrics
    interval: 30s
```

---

## Pod Watching and State Sync

### Watch Mechanism

```mermaid
sequenceDiagram
    participant KS as KubeScheduler
    participant API as K8s API Server
    participant Pod
    participant RQ as result_queue
    participant Exec as Executor
    
    Note over KS: Start watch stream
    KS->>API: GET /api/v1/namespaces/airflow/pods?watch=true
    API->>KS: HTTP 200 (chunked transfer)
    
    loop Watch stream
        Pod->>Pod: State changes
        API-->>KS: MODIFIED event {phase: Running}
        KS->>KS: Process event
        
        Pod->>Pod: Task completes
        API-->>KS: MODIFIED event {phase: Succeeded}
        KS->>KS: Extract result
        KS->>RQ: put(KubernetesResults)
    end
    
    Note over Exec: Scheduler sync()
    Exec->>RQ: get_nowait()
    RQ->>Exec: KubernetesResults
    Exec->>Exec: _change_state()
```

### Resource Version Tracking

**Purpose**: Efficient polling without missing events

```python
# Stored in AirflowKubernetesScheduler
resource_version = {
    'airflow': '12345',      # Last seen version in 'airflow' namespace
    'airflow-prod': '67890'  # If multi-namespace mode
}

# Watch request includes resourceVersion
API.list_namespaced_pod(
    namespace='airflow',
    watch=True,
    resource_version=resource_version['airflow']
)
```

**Benefits**:
- Only receive events since last check
- Avoid re-processing old events
- Efficient even with many pods

### Event Processing

```mermaid
flowchart TD
    Event[Pod Event Received] --> Type{Event type?}
    
    Type -->|ADDED| Check1[Check if we created it]
    Type -->|MODIFIED| Check2[Check phase change]
    Type -->|DELETED| Check3[Check if task running]
    
    Check1 -->|Yes| Ignore1[Ignore - we know about it]
    Check1 -->|No| Adopt[Attempt pod adoption]
    
    Check2 -->|Pending->Running| Log1[Log transition]
    Check2 -->|Running->Succeeded| Complete[Mark task SUCCESS]
    Check2 -->|Running->Failed| Fail[Mark task FAILED]
    Check2 -->|Other| Log2[Log event]
    
    Check3 -->|Yes| Unexpected[Log unexpected deletion]
    Check3 -->|No| Ignore2[Normal cleanup]
    
    Complete --> PutResult[Put in result_queue]
    Fail --> PutResult
    
    style Event fill:#4ecdc4
    style Complete fill:#b2f2bb
    style Fail fill:#ffe3e3
    style PutResult fill:#ffd93d
```

### Pod Adoption

**Scenario**: Scheduler restarts, existing pods still running

```python
def adopt_launched_task(self, pod: k8s.V1Pod) -> None:
    """
    Adopt a pod launched by a previous executor instance.
    
    - Extract task info from labels
    - Add to running set
    - Continue watching
    """
    annotations = pod.metadata.annotations
    dag_id = annotations.get('dag_id')
    task_id = annotations.get('task_id')
    logical_date = annotations.get('logical_date')
    
    key = TaskInstanceKey(dag_id, task_id, logical_date, try_number)
    self.running.add(key)
    self.log.info(f"Adopted pod {pod.metadata.name} for task {key}")
```

**Adoption Flow**:
```mermaid
flowchart TD
    Start([Scheduler starts]) --> List[List all pods with label]
    List --> Filter[Filter by airflow-worker=true]
    Filter --> Loop{For each pod}
    
    Loop -->|Has annotations| Extract[Extract task info]
    Loop -->|No annotations| Skip[Skip - not adoptable]
    
    Extract --> InDB{Task in DB?}
    InDB -->|Yes, RUNNING| Adopt[Add to running set]
    InDB -->|Yes, other state| Check[Check pod phase]
    InDB -->|No| Cleanup[Mark for cleanup]
    
    Adopt --> Watch[Start watching]
    Check --> Watch
    Cleanup --> Delete[Delete pod]
    
    Skip --> Next
    Watch --> Next
    Delete --> Next
    Next --> Loop
    
    style Start fill:#4ecdc4
    style Adopt fill:#b2f2bb
    style Cleanup fill:#ffe3e3
```

---

## Resource Management

### Resource Requests and Limits

**Requests vs Limits**:

| Aspect | Requests | Limits |
|--------|----------|--------|
| **Purpose** | Scheduling decision | Enforcement |
| **Guaranteed** | Yes | No (best effort) |
| **Behavior** | Pod won't schedule if node lacks resources | Pod killed if exceeded |
| **CPU** | Throttled if exceeded | Throttled at limit |
| **Memory** | Guaranteed amount | OOMKilled if exceeded |

**Configuration**:
```ini
[kubernetes_executor]
worker_container_repository = apache/airflow
worker_container_tag = 2.7.3
namespace = airflow

# Default pod resources
worker_pods_pending_timeout = 300
worker_pods_pending_timeout_batch_size = 100
worker_pods_queued_check_interval = 60

# Cleanup
delete_worker_pods = True
delete_worker_pods_on_success = True
delete_worker_pods_on_failure = False
```

### Pod Lifecycle Configuration

```ini
[kubernetes_executor]
# How long to wait before deleting succeeded pods
delete_worker_pods = True
delete_worker_pods_on_success = True

# Keep failed pods for debugging
delete_worker_pods_on_failure = False

# Pending pod timeout (seconds)
worker_pods_pending_timeout = 300

# Check interval
worker_pods_queued_check_interval = 60
```

### Multi-Namespace Mode

**Enable multiple namespaces**:
```ini
[kubernetes_executor]
multi_namespace_mode = True
multi_namespace_mode_namespace_list = airflow-prod,airflow-dev,airflow-test
```

**Or allow all namespaces** (leave list empty):
```ini
multi_namespace_mode = True
multi_namespace_mode_namespace_list =
```

**Benefits**:
- Isolate teams/environments
- Different resource quotas per namespace
- Better cost tracking

**Considerations**:
- Requires cluster-wide permissions (or per-namespace RBAC)
- More complex monitoring
- Need to handle namespace in task routing

### Resource Quotas

**Example namespace quota**:
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: airflow-quota
  namespace: airflow
spec:
  hard:
    requests.cpu: "100"        # Max 100 CPUs requested
    requests.memory: "200Gi"   # Max 200 GB memory requested
    limits.cpu: "200"          # Max 200 CPUs limit
    limits.memory: "400Gi"     # Max 400 GB memory limit
    pods: "500"                # Max 500 pods
```

**When quota exceeded**:
- Pod creation returns HTTP 403
- Executor retries with exponential backoff
- Task stays in QUEUED state
- Check `airflow.executors.executor_loader.stats.kubernetes_executor_queued_tasks` metric

---

## Debugging Guide

### Common Issues and Solutions

#### Issue 1: Task Stuck in QUEUED State

**Symptoms**:
- Task shows QUEUED in UI
- No pod created in Kubernetes

**Debug Steps**:

```bash
# 1. Check if executor is running
kubectl get pods -n airflow -l component=scheduler

# 2. Check scheduler logs
kubectl logs -n airflow <scheduler-pod> | grep -i kubernetes

# 3. Check task_queue size (in logs)
# Look for: "task_queue size: X"

# 4. Check API server accessibility
kubectl cluster-info

# 5. Check RBAC permissions
kubectl auth can-i create pods --namespace=airflow --as=system:serviceaccount:airflow:airflow-worker
```

**Common Causes**:

| Cause | Solution |
|-------|----------|
| **Executor not started** | Check scheduler pod is running |
| **API connection error** | Verify kubeconfig, check network |
| **RBAC permission denied** | Update ServiceAccount permissions |
| **Namespace doesn't exist** | Create namespace or fix config |
| **Resource quota exceeded** | Increase quota or free resources |

**Solution Example**:
```yaml
# Fix RBAC
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: airflow-worker
  namespace: airflow
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log", "pods/exec"]
  verbs: ["create", "get", "list", "watch", "delete", "patch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: airflow-worker
  namespace: airflow
subjects:
- kind: ServiceAccount
  name: airflow-worker
  namespace: airflow
roleRef:
  kind: Role
  name: airflow-worker
  apiGroup: rbac.authorization.k8s.io
```

#### Issue 2: Pod Stuck in Pending State

**Symptoms**:
- Pod created but never runs
- Pod phase: Pending
- Task stuck in RUNNING state in Airflow

**Debug Steps**:

```bash
# 1. Get pod details
kubectl get pod <pod-name> -n airflow

# 2. Check why pending
kubectl describe pod <pod-name> -n airflow

# Look for events at bottom:
# - "Insufficient memory"
# - "Insufficient cpu"
# - "ImagePullBackOff"
# - "0/3 nodes available: pod didn't match node selector"

# 3. Check pod events
kubectl get events -n airflow --field-selector involvedObject.name=<pod-name>

# 4. Check node capacity
kubectl top nodes
kubectl describe nodes | grep -A 5 "Allocated resources"
```

**Common Causes**:

| Cause | Event Message | Solution |
|-------|---------------|----------|
| **Insufficient resources** | "Insufficient cpu/memory" | Scale cluster or reduce requests |
| **Image pull error** | "ImagePullBackOff" | Check image name, credentials |
| **Node selector mismatch** | "pod didn't match node selector" | Fix node selector or add labels |
| **Toleration missing** | "node(s) had taint" | Add tolerations for tainted nodes |
| **PVC not bound** | "pod has unbound immediate PVCs" | Create PV or fix PVC |

**Solution Examples**:

```python
# Reduce resource requests
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            containers=[k8s.V1Container(
                name="base",
                resources=k8s.V1ResourceRequirements(
                    requests={"memory": "512Mi", "cpu": "0.5"},
                )
            )]
        )
    )
}

# Or scale cluster
kubectl scale deployment worker-nodes --replicas=5
```

#### Issue 3: Pod Fails with OOMKilled

**Symptoms**:
- Pod exits with Error
- Container exit code: 137
- Last state reason: OOMKilled

**Debug Steps**:

```bash
# 1. Check pod status
kubectl get pod <pod-name> -n airflow -o json | jq '.status.containerStatuses[0].lastState'

# Output:
# {
#   "terminated": {
#     "exitCode": 137,
#     "reason": "OOMKilled"
#   }
# }

# 2. Check memory usage (if pod still exists)
kubectl top pod <pod-name> -n airflow

# 3. Check task logs for memory-intensive operations
kubectl logs <pod-name> -n airflow
```

**Solutions**:

1. **Increase memory limit**:
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            containers=[k8s.V1Container(
                name="base",
                resources=k8s.V1ResourceRequirements(
                    limits={"memory": "4Gi"},  # Was 1Gi
                )
            )]
        )
    )
}
```

2. **Optimize task code**:
```python
# Bad: Load entire dataset into memory
df = pd.read_csv("large_file.csv")  # 10 GB!

# Good: Process in chunks
for chunk in pd.read_csv("large_file.csv", chunksize=10000):
    process(chunk)
```

3. **Use persistent storage**:
```python
# Store intermediate results on disk
with open("/tmp/intermediate.parquet", "wb") as f:
    df.to_parquet(f)
```

#### Issue 4: Logs Not Available

**Symptoms**:
- Airflow UI shows "Log not found"
- Pod completed/deleted

**Debug Steps**:

```bash
# 1. Check if remote logging configured
airflow config get-value logging remote_logging
# Should be: True

# 2. Check remote base path
airflow config get-value logging remote_base_log_folder
# Example: s3://my-bucket/airflow-logs

# 3. Check S3/GCS directly
# S3
aws s3 ls s3://my-bucket/airflow-logs/dag_id/task_id/

# GCS
gsutil ls gs://my-bucket/airflow-logs/dag_id/task_id/

# 4. If pod still exists, get logs from kubectl
kubectl logs <pod-name> -n airflow
```

**Solutions**:

1. **Enable remote logging** (config):
```ini
[logging]
remote_logging = True
remote_base_log_folder = s3://my-bucket/airflow-logs
remote_log_conn_id = aws_default
encrypt_s3_logs = False
```

2. **Configure connection**:
```bash
airflow connections add aws_default   --conn-type aws   --conn-extra '{
    "aws_access_key_id": "AKIA...",
    "aws_secret_access_key": "...",
    "region_name": "us-east-1"
  }'
```

3. **Mount logs volume** (for local access):
```yaml
volumes:
  - name: logs
    persistentVolumeClaim:
      claimName: airflow-logs

volumeMounts:
  - name: logs
    mountPath: /opt/airflow/logs
```

#### Issue 5: Image Pull Errors

**Symptoms**:
- Pod stuck in ImagePullBackOff or ErrImagePull
- Task never starts

**Debug Steps**:

```bash
# 1. Check pod events
kubectl describe pod <pod-name> -n airflow

# Common messages:
# - "Failed to pull image: 404 Not Found"
# - "Failed to pull image: unauthorized"
# - "Failed to pull image: timeout"

# 2. Check image exists
docker pull <image-name>:<tag>

# 3. Check imagePullSecrets configured
kubectl get pod <pod-name> -n airflow -o json | jq '.spec.imagePullSecrets'
```

**Common Causes**:

| Error | Cause | Solution |
|-------|-------|----------|
| **404 Not Found** | Image doesn't exist | Fix image name/tag |
| **unauthorized** | No pull credentials | Add imagePullSecret |
| **timeout** | Network/registry issue | Check connectivity, retry |
| **manifest unknown** | Tag doesn't exist | Check available tags |

**Solutions**:

1. **Add imagePullSecret**:
```bash
# Create secret
kubectl create secret docker-registry regcred   --docker-server=my-registry.com   --docker-username=myuser   --docker-password=mypass   --docker-email=me@example.com   -n airflow
```

2. **Use in pod template**:
```yaml
spec:
  imagePullSecrets:
  - name: regcred
  containers:
  - name: base
    image: my-registry.com/airflow:custom
```

3. **Or in executor_config**:
```python
executor_config={
    "pod_override": k8s.V1Pod(
        spec=k8s.V1PodSpec(
            image_pull_secrets=[k8s.V1LocalObjectReference(name="regcred")],
            containers=[k8s.V1Container(
                name="base",
                image="my-registry.com/airflow:custom",
            )]
        )
    )
}
```

### Debugging Tools

#### 1. Pod Inspection

```bash
# List all Airflow worker pods
kubectl get pods -n airflow -l airflow-worker=true

# Get pod details
kubectl describe pod <pod-name> -n airflow

# Get pod YAML
kubectl get pod <pod-name> -n airflow -o yaml

# Get pod logs
kubectl logs <pod-name> -n airflow -f

# Get previous pod logs (if restarted)
kubectl logs <pod-name> -n airflow --previous

# Exec into running pod
kubectl exec -it <pod-name> -n airflow -- /bin/bash
```

#### 2. Task State Queries

```sql
-- Check task state
SELECT dag_id, task_id, state, start_date, end_date, duration
FROM task_instance
WHERE dag_id = 'my_dag'
  AND task_id = 'my_task'
ORDER BY start_date DESC
LIMIT 10;

-- Find stuck tasks
SELECT dag_id, task_id, state, start_date,
       NOW() - start_date AS stuck_duration
FROM task_instance
WHERE state = 'running'
  AND start_date < NOW() - INTERVAL '1 hour'
ORDER BY start_date;

-- Check executor queue
SELECT dag_id, task_id, state, queued_dttm,
       NOW() - queued_dttm AS queued_duration
FROM task_instance
WHERE state = 'queued'
ORDER BY queued_dttm;
```

#### 3. Kubernetes Events

```bash
# Get recent events for namespace
kubectl get events -n airflow --sort-by='.lastTimestamp' | tail -20

# Filter by pod
kubectl get events -n airflow   --field-selector involvedObject.name=<pod-name>

# Filter by reason
kubectl get events -n airflow   --field-selector reason=FailedScheduling

# Watch events live
kubectl get events -n airflow --watch
```

#### 4. Resource Usage

```bash
# Node resources
kubectl top nodes

# Pod resources
kubectl top pods -n airflow

# Specific pod
kubectl top pod <pod-name> -n airflow

# Node allocatable resources
kubectl describe nodes | grep -A 7 "Allocated resources"
```

#### 5. Airflow CLI Commands

```bash
# List tasks
airflow tasks list my_dag

# Test task (don't update DB)
airflow tasks test my_dag my_task 2024-01-01

# Run task (update DB)
airflow tasks run my_dag my_task 2024-01-01

# Clear task state
airflow tasks clear my_dag -t my_task -s 2024-01-01 -e 2024-01-02

# Check executor config
airflow config get-value kubernetes_executor namespace
airflow config get-value kubernetes_executor worker_container_repository
```

### Performance Optimization

#### 1. Image Optimization

**Problem**: Slow pod startup due to large images

**Solutions**:

```dockerfile
# Bad: Large base image
FROM python:3.11
RUN pip install apache-airflow[all]

# Good: Slim image with only needed extras
FROM python:3.11-slim
RUN pip install apache-airflow[postgres,kubernetes]==2.7.3

# Better: Pre-built official image
FROM apache/airflow:2.7.3-python3.11

# Best: Multi-stage build
FROM python:3.11 AS builder
COPY requirements.txt .
RUN pip wheel --no-cache-dir -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /root/.cache /root/.cache
RUN pip install --no-index --find-links=/root/.cache apache-airflow
```

**Caching strategies**:
```yaml
# Always pull (slow but fresh)
imagePullPolicy: Always

# Pull if not cached (default)
imagePullPolicy: IfNotPresent

# Never pull (fastest, must pre-pull)
imagePullPolicy: Never
```

#### 2. Resource Right-Sizing

**Monitor actual usage**:
```bash
# Get resource usage for completed tasks
kubectl top pods -n airflow --containers | grep my-dag

# Check historical usage (if metrics-server with history)
kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespaces/airflow/pods/<pod-name>
```

**Right-size requests**:
```python
# Over-provisioned (wastes cluster capacity)
executor_config={"pod_override": k8s.V1Pod(spec=k8s.V1PodSpec(
    containers=[k8s.V1Container(name="base",
        resources=k8s.V1ResourceRequirements(
            requests={"memory": "8Gi", "cpu": "4"}  # Task only uses 1Gi, 0.5 CPU
        )
    )]
))}

# Right-sized
executor_config={"pod_override": k8s.V1Pod(spec=k8s.V1PodSpec(
    containers=[k8s.V1Container(name="base",
        resources=k8s.V1ResourceRequirements(
            requests={"memory": "1Gi", "cpu": "0.5"},
            limits={"memory": "2Gi", "cpu": "1"}  # Some headroom
        )
    )]
))}
```

#### 3. Parallelism Tuning

```ini
[kubernetes_executor]
# Max concurrent pods
parallelism = 32

# Batch size for pod creation
worker_pods_creation_batch_size = 10

# Check interval for queued pods
worker_pods_queued_check_interval = 30
```

**Tradeoffs**:
- Higher parallelism = More throughput, more cluster load
- Lower parallelism = Less cluster load, longer DAG completion

**Rule of thumb**: `parallelism` ≈ (avg concurrent tasks) × 1.2

#### 4. DAG Loading Optimization

**Problem**: Pods spend time loading DAGs

**Solutions**:

1. **Use DAG serialization** (avoid file parsing):
```ini
[core]
store_dag_code = True
load_examples = False
min_serialized_dag_update_interval = 30
```

2. **Optimize DAG files**:
```python
# Bad: Heavy imports at module level
import pandas as pd
import tensorflow as tf

@dag(...)
def my_dag():
    pass

# Good: Lazy imports in tasks
@dag(...)
def my_dag():
    @task
    def process():
        import pandas as pd  # Only imported when task runs
        ...
```

3. **Reduce DAG count**:
- Combine related workflows
- Use dynamic task mapping instead of multiple DAGs
- Archive unused DAGs

---

## Summary Checklist

### Task Execution Checklist

**Before task runs**:
- ☐ Kubernetes cluster accessible
- ☐ Namespace exists
- ☐ ServiceAccount has pod create/delete permissions
- ☐ Resource quotas not exceeded
- ☐ Image exists and pullable
- ☐ PersistentVolumes created and bound
- ☐ Database connection configured
- ☐ Remote logging configured (production)

**During task execution**:
- ☐ Pod created successfully
- ☐ Pod scheduled to node
- ☐ Image pulled
- ☐ Container started
- ☐ Task state updates to RUNNING
- ☐ Logs are being written
- ☐ No OOMKilled events
- ☐ Database connections healthy

**After task execution**:
- ☐ Task state is SUCCESS/FAILED
- ☐ XCom pushed (if needed)
- ☐ Logs uploaded to remote storage
- ☐ Pod cleaned up (if configured)
- ☐ No orphaned pods remaining

### Key Files Reference

| Component | File | Key Methods/Classes |
|-----------|------|---------------------|
| **KubernetesExecutor** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor.py` | `execute_async()`, `sync()`, `adopt_launched_task()` |
| **AirflowKubernetesScheduler** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor_utils.py` | `run_next()`, `sync()`, `_watch_pods()` |
| **PodGenerator** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/pod_generator.py` | `construct_pod()`, `reconcile_pods()` |
| **KubeConfig** | `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/kube_config.py` | Configuration loading |

### Monitoring Endpoints

**Health checks**:
- Scheduler: `curl http://scheduler:8080/health`
- Kubernetes API: `kubectl cluster-info`
- Database: `kubectl exec -it <pod> -- airflow db check`

**Metrics**:
- Active pods: `kubectl get pods -n airflow -l airflow-worker=true | grep Running | wc -l`
- Pending pods: `kubectl get pods -n airflow -l airflow-worker=true --field-selector status.phase=Pending`
- Resource usage: `kubectl top pods -n airflow`

**Logs**:
- Scheduler logs: `kubectl logs -n airflow <scheduler-pod> -f`
- Task logs: `kubectl logs -n airflow <task-pod> -f`
- Kubernetes events: `kubectl get events -n airflow --watch`

---

**Document version**: 1.0  
**Last updated**: 2024  
**For**: Apache Airflow with KubernetesExecutor

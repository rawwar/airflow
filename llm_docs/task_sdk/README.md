# Apache Airflow Task SDK Documentation

Comprehensive documentation for the Task SDK introduced in Airflow 3.0 for isolated task execution.

## 📚 Documentation Files

### Main Documentation
- **[`task_sdk_architecture.md`](task_sdk_architecture.md)** - Complete architecture and lifecycle (1,260+ lines, 9 Mermaid diagrams)

### Excalidraw Diagrams
- **[`excalidraw/README.md`](excalidraw/README.md)** - Diagram usage guide

---

## 🎯 Quick Overview

### What is the Task SDK?

The **Task SDK** is a standalone package (`apache-airflow-task-sdk`) that enables:

- **Isolated Task Execution** - Tasks run in separate processes from scheduler
- **Reduced Dependencies** - No full Airflow installation needed for tasks
- **Better Security** - User code never sees JWT authentication tokens
- **Improved Performance** - Fewer HTTP connections via supervisor proxy

### Two-Process Architecture

```
[Scheduler/Executor]
         ↓
    [Supervisor]  ←→ HTTP (with JWT) → [API Server]
         ↓
   Socket (msgpack)
         ↓
   [Task Runner]  (user code)
```

**Supervisor**: Trusted process that handles authentication and API communication
**Task Runner**: Subprocess that executes user\'s operator code

---

## ⚡ Key Features

### 1. Security Isolation
- JWT token stays in supervisor process
- User code communicates via local socket
- No direct API access from task code

### 2. Communication Protocol
- Binary msgpack over stdin socket
- Request-response pattern
- Type-safe with Pydantic models

### 3. Lazy Loading
- Variables fetched on demand
- Connections retrieved when accessed
- XComs pulled only when requested

### 4. API Proxy
- All API calls go through supervisor
- Reduces HTTP connection count
- Centralizes authentication

---

## 📚 Architecture Components

### Module Structure

```
airflow.sdk/
├── definitions/        # DAG definition interfaces
│   ├── dag.py
│   ├── operator.py
│   ├── taskgroup.py
│   ├── decorators/
│   └── asset/
├── bases/              # Base classes
│   ├── operator.py     # BaseOperator
│   ├── hook.py         # BaseHook
│   └── sensor.py       # BaseSensor
├── execution_time/     # Runtime execution
│   ├── supervisor.py   # Main entry point
│   ├── task_runner.py  # Task execution
│   ├── comms.py        # Communication protocol
│   ├── context.py      # Runtime context
│   └── xcom.py         # XCom operations
├── api/                # API client
│   ├── client.py       # HTTP client
│   └── datamodels/     # Pydantic models
└── io/                 # Object store
    ├── fs.py
    └── store.py
```

---

## 🔄 Task Execution Lifecycle

### 1. Supervisor Start
- Executor starts supervisor process
- Supervisor authenticates with API (JWT)
- Retrieves task metadata

### 2. Task Runner Fork
- Supervisor creates socketpair
- Forks task_runner.py subprocess
- Sends startup details via socket

### 3. Task Execution
- Task runner loads DAG bundle
- Builds execution context
- Runs `operator.execute(context)`

### 4. Resource Requests
- Task requests XCom via socket
- Supervisor proxies to API
- Response returned via socket

### 5. Completion
- Task sends SucceedTask message
- Supervisor updates state via API
- Both processes exit

---

## 📝 Example Usage

### Defining a DAG

```python
from airflow.sdk.definitions import DAG
from airflow.sdk.definitions.decorators import task
from datetime import datetime

with DAG(
    dag_id="example_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
) as dag:
    
    @task
    def extract():
        return {"data": [1, 2, 3]}
    
    @task
    def transform(data: dict):
        return {"sum": sum(data["data"])}
    
    @task
    def load(result: dict):
        print(f"Result: {result}")
    
    load(transform(extract()))
```

### Custom Operator

```python
from airflow.sdk.bases.operator import BaseOperator
from airflow.sdk.definitions.context import Context

class MyOperator(BaseOperator):
    def __init__(self, my_param: str, **kwargs):
        super().__init__(**kwargs)
        self.my_param = my_param
    
    def execute(self, context: Context):
        # Access XCom
        upstream_data = context.ti.xcom_pull(
            task_ids="upstream_task"
        )
        
        # Access Variable (lazy-loaded)
        my_var = context.var.value.my_variable_key
        
        # Access Connection
        conn = context.conn.postgres_default
        
        # Process and return
        result = self.process(upstream_data, my_var)
        return result
```

---

## 💬 Communication Protocol

### Message Format

```
+-------------------+
| 4 bytes: length   |  (big-endian uint32)
+-------------------+
| N bytes: msgpack  |  (msgpack-encoded message)
+-------------------+
```

### Request Types

| Request | Purpose |
|---------|----------|
| `GetXCom` | Retrieve XCom value |
| `GetVariable` | Get Airflow variable |
| `GetConnection` | Get connection details |
| `GetAssetByName` | Get asset metadata |
| `GetDagRunState` | Get DAG run state |
| `SucceedTask` | Mark task SUCCESS |
| `DeferTask` | Defer to triggerer |
| `RetryTask` | Mark for retry |

### Example Message

```python
# Task → Supervisor
{
    "type": "GetXCom",
    "key": "return_value",
    "task_id": "upstream",
    "dag_id": "my_dag",
    "run_id": "manual__2024-01-15T10:00:00+00:00"
}

# Supervisor → Task
{
    "type": "XComResult",
    "value": {"data": [1, 2, 3]},
    "key": "return_value"
}
```

---

## 🔑 API Client

### Endpoints

**Task Execution API** (`/execution/api/v1/`):

| Method | Endpoint | Purpose |
|--------|----------|----------|
| GET | `/tasks/{id}/run` | Get startup details |
| PATCH | `/tasks/{id}/heartbeat` | Send heartbeat |
| PATCH | `/tasks/{id}/state` | Update state |
| GET | `/xcoms` | Get XCom value |
| PUT | `/xcoms` | Set XCom value |
| GET | `/variables/{key}` | Get variable |
| GET | `/connections/{id}` | Get connection |

### Authentication

**JWT Token**:
- Generated by scheduler for each task instance try
- Passed to supervisor via environment
- Supervisor includes in all API requests
- Task runner never sees token

---

## 🐛 Debugging

### Enable Debug Logging

```python
# In supervisor or task_runner
import structlog
structlog.configure(log_level="DEBUG")

# Logs all msgpack frames:
# DEBUG - Sending to task: {"type": "StartupDetails", ...}
# DEBUG - Received from task: {"type": "GetXCom", ...}
```

### Test API Client

```python
from airflow.sdk.api.client import Client
from uuid import UUID

client = Client(
    base_url="http://localhost:8080/execution/api/v1",
    token="<JWT>"
)

# Get task instance
ti = client.task_instances.get(UUID("task-uuid"))
print(ti.state)

# Get XCom
xcom = client.xcoms.get(
    dag_id="my_dag",
    task_id="my_task",
    run_id="manual__..."
)
print(xcom.value)
```

### Test Communication

```python
import msgspec
import struct

# Encode msgpack frame
from airflow.sdk.execution_time.comms import GetXCom
request = GetXCom(
    key="return_value",
    task_id="upstream",
    dag_id="my_dag",
    run_id="manual__..."
)

encoded = msgspec.msgpack.encode(request)
length = struct.pack(">I", len(encoded))
frame = length + encoded

print(f"Frame: {len(frame)} bytes")
print(frame.hex())
```

---

## 🚨 Common Issues

### Issue: Task Process Not Starting

**Check**:
```bash
# Is SDK installed?
python -m airflow.sdk.execution_time.task_runner --help

# Check supervisor logs
grep "supervisor" /opt/airflow/logs/dag/task/*/1.log
```

**Solution**: Install `apache-airflow-task-sdk`

### Issue: XCom Not Found

**Check**:
```bash
# Query API directly
curl -H "Authorization: Bearer $TOKEN" \
     "http://localhost:8080/execution/api/v1/xcoms?task_id=upstream"
```

**Solution**: Ensure upstream task completed successfully

### Issue: Communication Errors

**Check**:
```bash
# Enable debug logging
export __AIRFLOW_SDK_LOG_LEVEL=DEBUG
```

**Solution**: Check msgpack version compatibility

---

## 📈 Performance

### Overhead

| Phase | Duration |
|-------|----------|
| Supervisor start | 0.1-0.2s |
| API authentication | 0.1-0.3s |
| Fork task_runner | 0.1s |
| Load DAG bundle | 0.2-0.5s |
| Build context | 0.05-0.1s |
| Per XCom request | 0.01-0.05s |
| State update | 0.1-0.2s |

**Total Overhead**: ~0.7-1.5s per task

### Optimization

- **Bundle caching**: Reuse parsed DAG bundles
- **Connection pooling**: Supervisor reuses HTTP connections
- **Lazy loading**: Variables/Connections fetched only when needed
- **Binary protocol**: msgpack faster than JSON

---

## 🔗 Related Documentation

- [Task Execution on CeleryExecutor](../task_execution/) - How Celery executor works
- [Task Execution on KubernetesExecutor](../task_execution_k8s/) - K8s pod-based execution
- [Deferrable Tasks](../task_execution_deferrable/) - Triggerer integration
- [Scheduler](../scheduler/) - How tasks get scheduled

---

## 📖 Source Code

### Key Files

**Supervisor**:
- `task-sdk/src/airflow/sdk/execution_time/supervisor.py` - Main entry
- `task-sdk/src/airflow/sdk/execution_time/comms.py` - Protocol

**Task Runner**:
- `task-sdk/src/airflow/sdk/execution_time/task_runner.py` - Execution
- `task-sdk/src/airflow/sdk/execution_time/context.py` - Context

**API Client**:
- `task-sdk/src/airflow/sdk/api/client.py` - HTTP client
- `task-sdk/src/airflow/sdk/api/datamodels/` - Models

**Definitions**:
- `task-sdk/src/airflow/sdk/definitions/dag.py` - DAG class
- `task-sdk/src/airflow/sdk/bases/operator.py` - BaseOperator

---

## 📝 Summary

**Key Concepts**:
- **Two-process model**: Supervisor (trusted) + Task Runner (user code)
- **Socket communication**: Binary msgpack over stdin
- **JWT isolation**: User code never sees auth tokens
- **API proxy**: All requests go through supervisor
- **Lazy loading**: Resources fetched on demand
- **Type safety**: Pydantic models for all API data

**Benefits**:
- ✓ Better security (token isolation)
- ✓ Fewer HTTP connections
- ✓ Reduced dependencies for tasks
- ✓ Cleaner architecture
- ✓ Easier to test and debug

**Next Steps**:
1. Review main documentation for detailed architecture
2. Explore source code in `task-sdk/src/`
3. Test custom operators with Task SDK
4. Monitor supervisor logs for debugging

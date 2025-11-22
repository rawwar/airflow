# Airflow Listeners and OpenLineage Documentation

Comprehensive documentation for understanding Airflow's listener system and OpenLineage data lineage integration.

## 📚 Documentation Files

### Main Documentation
- **[`listeners_and_openlineage_lifecycle.md`](listeners_and_openlineage_lifecycle.md)** - Complete lifecycle documentation (17+ Mermaid diagrams, 2,200+ lines)

### Excalidraw Diagrams
- **[`excalidraw/01_complete_flow.excalidraw`](excalidraw/01_complete_flow.excalidraw)** - End-to-end event flow from task start to backend storage
- **[`excalidraw/02_listener_registration.excalidraw`](excalidraw/02_listener_registration.excalidraw)** - Plugin discovery and registration process
- **[`excalidraw/README.md`](excalidraw/README.md)** - How to use and edit diagrams

---

## 🎯 Quick Reference

### What Are Listeners?

Listeners are a pluggable system for monitoring Airflow lifecycle events:
- Task instance state changes (RUNNING, SUCCESS, FAILED)
- DAG run state changes
- Asset changes
- Import errors

### What Is OpenLineage?

OpenLineage is a standard for data lineage collection:
- Tracks data inputs/outputs for each task
- Records job metadata and execution details
- Captures facets (SQL queries, schemas, metrics)
- Sends events to configured backends

---

## 🔍 Architecture Overview

```
TaskInstance/DagRun (state change)
    ↓
get_listener_manager()
    ↓
PluginManager (pluggy)
    ↓ (broadcast to all registered listeners)
OpenLineageListener
    ↓
ExtractorManager
    ↓ (find and run extractor)
OperatorLineage (inputs, outputs, facets)
    ↓
OpenLineageAdapter
    ↓ (build RunEvent)
OpenLineageClient
    ↓ (emit)
Transport (HTTP/Kafka/File)
    ↓
Backend (Marquez/Egeria/Custom)
```

---

## ⚙️ Configuration

### Enable OpenLineage

**`airflow.cfg`**:
```ini
[openlineage]
disabled = False
namespace = production
transport = {"type": "http", "url": "http://marquez:5000"}
```

**OR use YAML config**:
```ini
[openlineage]
config_path = /opt/airflow/config/openlineage.yml
```

**`openlineage.yml`**:
```yaml
transport:
  type: http
  url: http://marquez:5000
  auth:
    type: api_key
    apiKey: ${MARQUEZ_API_KEY}
  timeout: 5.0

namespace: production
```

### Disable Specific Operators

```ini
[openlineage]
disabled_for_operators = SnowflakeOperator;BigQueryOperator
```

### Selective Enable Mode

```ini
[openlineage]
selective_enable = True
```

Then tag DAGs:
```python
dag = DAG(
    ...,
    tags=["openlineage"],
)
```

---

## 🐛 Debugging Commands

### Check Configuration

```python
from airflow.providers.openlineage import conf
print("Disabled:", conf.is_disabled())
print("Namespace:", conf.namespace())
print("Transport:", conf.transport())
```

### Check Listener Registration

```python
from airflow.listeners.listener import get_listener_manager
lm = get_listener_manager()
print("Has listeners:", lm.has_listeners)
print("Registered:", lm.pm.get_plugins())
```

### Test Event Emission

```python
from airflow.providers.openlineage.plugins.adapter import OpenLineageAdapter
from openlineage.client.event_v2 import RunEvent, RunState, Run, Job
from datetime import datetime

adapter = OpenLineageAdapter()
event = RunEvent(
    eventType=RunState.START,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId="test-run-id", facets={}),
    job=Job(namespace="test", name="test-job", facets={}),
    inputs=[],
    outputs=[]
)
adapter.emit(event)
```

### Check Scheduler Logs

```bash
grep "OpenLineage" /opt/airflow/logs/scheduler/latest/*.log
grep "error calling listener" /opt/airflow/logs/scheduler/latest/*.log -A 20
```

### Enable Debug Mode

```ini
[openlineage]
debug_mode = True

[logging]
logging_level = DEBUG
```

---

## 📊 Common SQL Queries

### Check Task Instance Metadata

```sql
SELECT
    dag_id,
    task_id,
    run_id,
    state,
    start_date,
    end_date,
    duration
FROM task_instance
WHERE dag_id = 'my_dag'
  AND run_id = 'manual__2024-01-15T10:00:00+00:00'
ORDER BY start_date DESC;
```

### Check XCom for Lineage Data

```sql
SELECT
    key,
    value,
    timestamp
FROM xcom
WHERE dag_id = 'my_dag'
  AND task_id = 'extract_task'
  AND run_id = 'manual__2024-01-15T10:00:00+00:00'
  AND key LIKE '%lineage%';
```

---

## 🚨 Troubleshooting

### Issue: Events Not Emitted

**Check**:
1. OpenLineage disabled? → `airflow config get-value openlineage disabled`
2. Transport configured? → `airflow config get-value openlineage transport`
3. Operator disabled? → Check `disabled_for_operators`
4. Selective mode? → Add `openlineage` tag to DAG
5. Backend reachable? → Test with `curl` or `telnet`

### Issue: Listener Errors in Logs

**Check**:
1. Full stack trace: `grep "error calling listener" -A 20 /path/to/logs`
2. Import errors: Missing dependencies?
3. Configuration errors: Invalid YAML/JSON?
4. Network errors: Backend down?

### Issue: Missing Lineage Data

**Check**:
1. Operator has `get_openlineage_facets_on_complete`?
2. Extractor registered for operator?
3. Operator configuration correct (connection IDs, table names)?

### Issue: High Latency

**Solutions**:
1. Use Kafka transport (async, non-blocking)
2. Increase timeout: `execution_timeout = 15`
3. Use file transport for dev: `transport = {"type": "file", "path": "/tmp/events.json"}`
4. Disable for heavy operators

---

## 📈 Performance

### Typical Overhead

| Phase | Duration |
|-------|----------|
| Listener hook call | 0.01-0.05s |
| Check disabled operators | 0.001s |
| Extract metadata | 0.1-0.3s |
| Build event | 0.05-0.1s |
| Emit to HTTP backend | 0.1-0.5s |
| **Total (START + COMPLETE)** | **0.5-2s** |

### Optimization Tips

1. **Use async transport** (Kafka)
2. **Disable for specific operators**
3. **Use selective enable mode**
4. **Reduce facet complexity**

---

## 🔗 Related Files

### Core Files
- `airflow/listeners/listener.py` - ListenerManager, registration
- `airflow/listeners/spec/taskinstance.py` - Task hook specifications
- `airflow/listeners/spec/dagrun.py` - DAG run hook specifications
- `airflow/models/taskinstance.py` - Hook invocation points
- `airflow/models/dagrun.py` - DAG run hook invocation

### OpenLineage Provider Files
- `providers/openlineage/src/airflow/providers/openlineage/plugins/listener.py` - OpenLineageListener implementation
- `providers/openlineage/src/airflow/providers/openlineage/plugins/adapter.py` - OpenLineageAdapter for event building
- `providers/openlineage/src/airflow/providers/openlineage/extractors/manager.py` - ExtractorManager
- `providers/openlineage/src/airflow/providers/openlineage/extractors/base.py` - BaseExtractor, DefaultExtractor
- `providers/openlineage/src/airflow/providers/openlineage/conf.py` - Configuration loading

---

## 📖 Further Reading

- [OpenLineage Specification](https://openlineage.io/docs/spec/)
- [Airflow Listeners Documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/listeners.html)
- [OpenLineage Airflow Provider](https://airflow.apache.org/docs/apache-airflow-providers-openlineage/stable/index.html)
- [Marquez (OpenLineage Backend)](https://marquezproject.ai/)

---

## 📝 Summary

**Key Concepts**:
- Listeners use **pluggy** framework for extensibility
- OpenLineage events are **not stored in Airflow DB**
- Event emission is **synchronous** but **failure-isolated**
- Configuration is **flexible** (YAML, airflow.cfg, env vars)
- Overhead is **minimal** with proper transport

**Next Steps**:
1. Review main documentation for detailed flows
2. Open Excalidraw diagrams for visual understanding
3. Configure transport for your lineage backend
4. Enable selective lineage for production
5. Monitor emission metrics

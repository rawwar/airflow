# Excalidraw Diagrams for Task SDK

This directory contains editable Excalidraw diagrams visualizing the Task SDK architecture and execution flow.

## 📝 Diagram Files

### 1. Two-Process Architecture
**File**: `01_two_process_architecture.excalidraw` (16KB)

**Shows**: High-level view of Supervisor and Task Runner processes with security boundaries

**Components**:
- Scheduler/Executor (starting point)
- Supervisor process (cyan) - Trusted, has JWT token
- Socket communication (orange) - msgpack protocol
- Task Runner process (green) - User code, no JWT
- API Server (yellow) - HTTP endpoints
- Database (gray) - Airflow metadata
- Security boundary showing Task Runner has NO direct API access

**Key Points**:
- Supervisor has JWT token, Task Runner does NOT
- All API calls proxied through Supervisor
- Communication via msgpack over socket (stdin)
- User code runs isolated in Task Runner process

---

### 2. Communication Protocol
**File**: `02_communication_protocol.excalidraw` (18KB)

**Shows**: msgpack frame format and request-response message types

**Components**:
- **Frame Format**:
  - 4 bytes: Length (big-endian uint32)
  - N bytes: msgpack payload
- **Request Examples** (Task → Supervisor):
  - GetXCom, GetVariable, GetConnection
  - GetAssetByName, GetAssetByUri
  - GetDagRunState, GetTaskStates
  - SucceedTask, DeferTask, RetryTask, FailTask
- **Response Examples** (Supervisor → Task):
  - XComResult, VariableResult, ConnectionResult
  - AssetResult, DagRunStateResult, TaskStatesResult
  - StartupDetails, ErrorResponse
- Example message showing GetXCom request structure

**Request-Response Flow**: Shows bidirectional communication between Task Runner and Supervisor

---

### 3. Task Execution Flow
**File**: `03_task_execution_flow.excalidraw` (20KB)

**Shows**: Complete lifecycle from supervisor start to task completion with timeline

**7 Execution Phases**:

1. **Supervisor Start** (t=0.2s) - Cyan
   - Authenticate with API
   - Get startup details
   - JWT token received

2. **Fork Process** (t=0.3s) - Cyan
   - Create socketpair
   - Fork task_runner.py
   - Send StartupDetails

3. **Load DAG** (t=0.6s) - Light Green
   - Load DAG bundle
   - Parse DAG file
   - Find operator

4. **Build Context** (t=0.7s) - Light Green
   - Create Context object
   - Lazy accessors
   - Template rendering

5. **Execute Task** (t=10s) - Green
   - operator.execute(context)
   - User code runs
   - Returns result

6. **Report State** (t=10.2s) - Cyan
   - Send SucceedTask
   - Supervisor updates API
   - PATCH /tasks/{id}/state

7. **Complete** (t=10.3s) - Pale Green
   - Both processes exit

**Resource Requests Box** (right side, orange):
Shows all possible resource requests during execution:
- XCom values
- Variables
- Connections
- Assets
- DAG Run state

All requests go via socket to Supervisor, which proxies to API.

---

## 🎨 Color Scheme

Consistent colors used across all diagrams:

| Color | Hex | Usage |
|-------|-----|-------|
| **Cyan** | #4ecdc4 | Supervisor process, trusted components |
| **Light Green** | #95e1d3 | Task Runner process, user code |
| **Pale Green** | #b2f2bb | Successful completion, operator execution |
| **Yellow** | #ffd93d | API Server, databases |
| **Orange** | #ffec99, #f08c00 | Sockets, communication, warnings |
| **Blue** | #d0ebff | Scheduler, protocol messages |
| **Gray** | #f8f9fa | Code examples, annotations |
| **Red** | #e03131 | Errors, denied access |

---

## 🛠️ How to Use

### Viewing Diagrams

**Option 1: Excalidraw Web App** (Recommended)
1. Go to https://excalidraw.com
2. Click "Open" in top-left
3. Select a `.excalidraw` file from this directory
4. View, zoom, pan, and explore

**Option 2: Excalidraw VS Code Extension**
1. Install "Excalidraw" extension in VS Code
2. Open any `.excalidraw` file
3. Diagrams render directly in editor

**Option 3: Excalidraw Desktop**
1. Download from https://github.com/excalidraw/excalidraw-desktop
2. Open `.excalidraw` files

### Editing Diagrams

1. **Open** in Excalidraw (web or desktop)
2. **Edit** elements:
   - Select elements with mouse
   - Move by dragging
   - Resize with corner handles
   - Edit text by double-clicking
3. **Add** new elements:
   - Rectangle, ellipse, arrow from toolbar
   - Text tool for annotations
4. **Save**: File → Save to save changes
5. **Export**: File → Export as PNG/SVG for embedding in docs

### Exporting for Documentation

**PNG Export** (for embedding in markdown):
```bash
# In Excalidraw web app:
# File → Export image → PNG
# Set scale to 2x for high DPI
# Download to llm_docs/task_sdk/images/
```

**SVG Export** (for scalable graphics):
```bash
# In Excalidraw web app:
# File → Export image → SVG
# Check "Embed scene" to preserve editability
```

---

## 📊 Diagram Structure

### Layout Principles

1. **Top-to-bottom flow**: Time/causality flows downward
2. **Color coding**: Consistent colors for component types
3. **Timeline annotations**: Execution times marked on diagrams
4. **Legend boxes**: Key points summarized at bottom
5. **Grouped components**: Related elements visually grouped

### Element Types

- **Rectangle**: Components, modules, processes
- **Rounded rectangle**: Phases, actions, states
- **Arrow**: Data/control flow, causality
- **Dashed line**: Optional, denied, or informational relationship
- **Text**: Labels, annotations, code snippets
- **Hachure fill**: Secondary/supporting components

---

## 🔄 Updating Diagrams

### When to Update

- **Code changes**: Task SDK API or protocol changes
- **New features**: Additional request types, new components
- **Clarifications**: User feedback, documentation gaps
- **Bug fixes**: Incorrect flows or missing components

### Update Process

1. **Open** diagram in Excalidraw
2. **Make changes** following color scheme and layout principles
3. **Save** as `.excalidraw` file
4. **Export** PNG to `images/` if embedding in markdown
5. **Update** this README if adding new diagrams
6. **Commit** changes to repository

---

## 📝 File Format

Excalidraw files are JSON with the following structure:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "type": "rectangle",
      "id": "unique_id",
      "x": 100,
      "y": 50,
      "width": 200,
      "height": 80,
      "fillStyle": "solid",
      "backgroundColor": "#4ecdc4",
      ...
    },
    ...
  ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    ...
  },
  "files": {}
}
```

**Key fields**:
- `elements`: Array of shapes, text, arrows
- `appState`: Canvas state (background, grid)
- `files`: Embedded images (if any)

---

## 🔗 Related Documentation

- **Main Task SDK docs**: [`../task_sdk_architecture.md`](../task_sdk_architecture.md)
- **README**: [`../README.md`](../README.md)
- **Other execution docs**: 
  - [`../../task_execution/`](../../task_execution/) - CeleryExecutor
  - [`../../task_execution_k8s/`](../../task_execution_k8s/) - KubernetesExecutor
  - [`../../task_execution_deferrable/`](../../task_execution_deferrable/) - Triggerer

---

## ❓ FAQ

**Q: Can I edit .excalidraw files in a text editor?**  
A: Yes, they\'re JSON files. But use Excalidraw app for visual editing.

**Q: How do I add new shapes?**  
A: In Excalidraw, use toolbar on left (rectangle, ellipse, arrow, text, etc.)

**Q: Can I embed images in diagrams?**  
A: Yes, drag PNG/JPG into Excalidraw canvas. Images are base64-encoded in JSON.

**Q: What\'s the msgpack format shown in diagram 02?**  
A: 4-byte big-endian length prefix + msgpack-encoded message body.

**Q: Why are timings shown in diagram 03?**  
A: To illustrate typical execution duration for each phase (total ~10s for task).

---

## 🐛 Issues

If diagrams don\'t render or have errors:

1. **Validate JSON**: Use `jq . < file.excalidraw` to check syntax
2. **Check version**: Ensure `"version": 2` is present
3. **Try web app**: https://excalidraw.com is most compatible
4. **Report issue**: Open GitHub issue with error details

---

## 📦 File Sizes

| File | Size | Elements |
|------|------|----------|
| `01_two_process_architecture.excalidraw` | ~16 KB | 25+ |
| `02_communication_protocol.excalidraw` | ~18 KB | 30+ |
| `03_task_execution_flow.excalidraw` | ~20 KB | 40+ |

**Total**: 3 diagrams, ~54 KB

---

## ✅ Diagram Checklist

When creating/updating diagrams:

- [x] Follows top-to-bottom flow
- [x] Uses consistent color scheme
- [x] Includes timeline annotations (where applicable)
- [x] Text is readable at 100% zoom
- [x] Arrows clearly show causality
- [x] Legend/key points included
- [x] Exported PNG is 2x scale
- [x] README updated with diagram description

---

**Status**: ✅ All Task SDK diagrams complete and ready for use.

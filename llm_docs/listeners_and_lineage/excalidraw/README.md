# Excalidraw Diagrams for Listeners and OpenLineage

This directory contains editable Excalidraw diagrams visualizing the Airflow listener system and OpenLineage event emission flow.

## 📝 Diagram Files

### 1. Complete Event Flow
**File**: `01_complete_flow.excalidraw`

**Shows**: End-to-end OpenLineage event emission from task start to backend storage

**Components**:
- Task starts (state=RUNNING)
- ListenerManager invocation
- PluginManager hook dispatch
- OpenLineageListener processing
- ExtractorManager metadata extraction
- OpenLineageAdapter event building
- OpenLineageClient emission
- Transport backend (HTTP/Kafka/File)

**Timeline**: Annotated with execution times (t=0.0s to t=0.50s)

**Color Coding**:
- Yellow (#ffd93d): Task/trigger point
- Cyan (#4ecdc4): Listener infrastructure
- Blue (#d0ebff): Plugin framework
- Green (#95e1d3, #b2f2bb): OpenLineage components
- Orange (#ffec99): Backend storage

---

### 2. Listener Registration
**File**: `02_listener_registration.excalidraw`

**Shows**: Plugin discovery and listener registration at Airflow startup

**Components**:
- Airflow startup trigger
- Plugin directory scan
- Python module loading
- AirflowPlugin class discovery
- Listener attribute extraction
- ListenerManager registration
- Example: OpenLineageProviderPlugin code

**Color Coding**:
- Cyan (#4ecdc4): Startup phase
- Blue (#d0ebff): Discovery/loading
- Green (#95e1d3, #b2f2bb): Registration
- Gray (#f8f9fa): Code example

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
# Download to llm_docs/listeners_and_lineage/images/
```

**SVG Export** (for scalable graphics):
```bash
# In Excalidraw web app:
# File → Export image → SVG
# Check "Embed scene" to preserve editability
```

---

## 🎨 Color Scheme

Consistent colors used across all diagrams:

| Color | Hex | Usage |
|-------|-----|-------|
| **Cyan** | #4ecdc4 | Listener infrastructure, core components |
| **Yellow** | #ffd93d | Task instances, trigger points, databases |
| **Green (light)** | #95e1d3 | OpenLineage components, success states |
| **Green (pale)** | #b2f2bb | Adapters, clients, output |
| **Red (light)** | #ffe3e3 | Errors, failures |
| **Orange** | #ffec99 | Backend storage, intermediate |
| **Blue** | #d0ebff | Plugin framework, transport |
| **Gray** | #f8f9fa | Code examples, annotations |

---

## 📊 Diagram Structure

### Layout Principles

1. **Top-to-bottom flow**: Time/causality flows downward
2. **Left-to-right**: Alternatives or parallel processes
3. **Grouped components**: Related elements grouped with visual proximity
4. **Timeline annotations**: Execution time annotations on right side
5. **Code examples**: Dashed boxes with monospace font

### Element Types

- **Rectangle**: Components, modules, classes
- **Rounded rectangle**: Processes, functions, actions
- **Arrow**: Data/control flow, causality
- **Dashed arrow**: Optional or informational relationship
- **Text**: Labels, annotations, code snippets
- **Dashed box**: Code examples, grouping

---

## 🔄 Updating Diagrams

### When to Update

- **Code changes**: Airflow listener API changes
- **New features**: Additional extractors, transports
- **Clarifications**: User feedback, documentation gaps
- **Bug fixes**: Incorrect flows or components

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

- **Main docs**: [`../listeners_and_openlineage_lifecycle.md`](../listeners_and_openlineage_lifecycle.md)
- **README**: [`../README.md`](../README.md)
- **Scheduler docs**: [`../../scheduler/`](../../scheduler/)
- **DAG run docs**: [`../../dag_run_lifecycle/`](../../dag_run_lifecycle/)
- **Task execution docs**: [`../../task_execution/`](../../task_execution/)

---

## ❓ FAQ

**Q: Can I edit .excalidraw files in a text editor?**  
A: Yes, they\'re JSON files. But use Excalidraw app for visual editing.

**Q: How do I add new shapes?**  
A: In Excalidraw, use toolbar on left (rectangle, ellipse, arrow, text, etc.)

**Q: Can I embed images in diagrams?**  
A: Yes, drag PNG/JPG into Excalidraw canvas. Images are base64-encoded in JSON.

**Q: What\'s the difference between .excalidraw and .excalidraw.svg?**  
A: `.excalidraw` is editable JSON. `.excalidraw.svg` is exported SVG with optional embedded scene for re-editing.

**Q: How do I share diagrams?**  
A: Export as PNG/SVG, or use Excalidraw\'s "Share" feature to generate a link.

---

## 🐛 Issues

If diagrams don\'t render or have errors:

1. **Validate JSON**: Use `jq . < file.excalidraw` to check syntax
2. **Check version**: Ensure `"version": 2` is present
3. **Try web app**: https://excalidraw.com is most compatible
4. **Report issue**: Open GitHub issue with error details

---

## 📝 Contributing

Contributions welcome! To add new diagrams:

1. Create diagram in Excalidraw (follow color scheme)
2. Export as `.excalidraw` to this directory
3. Export PNG to `images/` for embedding
4. Update this README with diagram description
5. Submit pull request

---

## 📦 File Sizes

| File | Size | Elements |
|------|------|----------|
| `01_complete_flow.excalidraw` | ~15 KB | 30+ |
| `02_listener_registration.excalidraw` | ~10 KB | 20+ |

**Note**: Sizes increase significantly if images are embedded.

---

## ✅ Diagram Checklist

When creating/updating diagrams:

- [ ] Follows top-to-bottom flow
- [ ] Uses consistent color scheme
- [ ] Includes timeline annotations (if applicable)
- [ ] Text is readable at 100% zoom
- [ ] Arrows clearly show causality
- [ ] Code examples use monospace font
- [ ] Exported PNG is 2x scale
- [ ] README updated with diagram description

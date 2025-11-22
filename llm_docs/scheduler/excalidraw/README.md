# Excalidraw Diagrams for Scheduler

This directory contains detailed Excalidraw diagrams for visualizing Airflow's scheduler behavior.

## Files

### 01_high_level_flow.excalidraw
**Topic**: High-level flow from DAG file to DAG run creation

**Elements**:
- 5 main components (DAG File, Dag Processor, DagModel Table, Scheduler, DAG Run Creation)
- Color-coded phases:
  - Dag Processor: Cyan (#4ecdc4)
  - DagModel Table: Yellow (#ffd93d) - THE KEY FIELD
  - Scheduler: Light green (#95e1d3)
  - DAG Run: Green (#b2f2bb)
- Shows `next_dagrun_create_after` calculation and storage
- Shows WHERE condition query from scheduler

**Key Visualization**: The orange dashed lines show the critical `next_dagrun_create_after` field flow

### 02_scheduler_loop_detailed.excalidraw
**Topic**: Complete scheduler loop with all decision points

**Elements**:
- Loop start/end visualization
- Query execution (yellow box)
- Decision diamonds:
  - Any DAGs found?
  - Run already exists?
  - max_active_runs reached?
  - More DAGs to process?
- Action boxes:
  - Create DagRun (green, emphasized with thick border)
  - Calculate next run (orange)
  - Commit transaction (green)
  - Start queued DagRuns (green)
  - Schedule task instances (green)
- Loop arrows showing:
  - Main flow (solid black)
  - Return to start (dashed blue)
  - Skip paths (dashed gray)

**Key Visualization**: Shows all three checks before creating a run and the continuous loop nature

## How to Use

### Opening in Excalidraw

1. **Online**: Visit https://excalidraw.com
2. **Click**: File → Open
3. **Select**: One of the `.excalidraw` files from this directory

### Editing

All diagrams are fully editable in Excalidraw:
- Move elements by dragging
- Resize boxes and shapes
- Change colors via element properties
- Add/remove arrows and connections
- Edit text by double-clicking

### Exporting

From Excalidraw, you can export to:
- PNG (for presentations)
- SVG (for scaling)
- Clipboard (for pasting into docs)

## Color Scheme

### Phase Colors:
- **Cyan (#4ecdc4)**: Dag Processor operations
- **Yellow (#ffd93d)**: DagModel/Database (emphasis on critical field)
- **Light Green (#95e1d3)**: Scheduler operations
- **Green (#b2f2bb)**: Success/Creation actions
- **Light Blue (#d0ebff)**: Iterative/Loop elements
- **Red (#ffe3e3)**: Critical decisions/conditions
- **Orange (#ffec99)**: Key field calculations
- **Gray (#e9ecef)**: Skip/No-op actions

### Arrow Colors:
- **Black (#1e1e1e)**: Main flow
- **Orange (#f08c00)**: Critical field flow (dashed)
- **Red (#e03131)**: Critical decision flow
- **Green (#2f9e44)**: Success path
- **Blue (#1971c2)**: Loop/Iteration (dashed)
- **Gray (#868e96)**: Skip/Alternative path (dashed)

## Diagram Specifications

### Element Types Used:
- **Rectangle**: Processes, actions, storage
- **Diamond**: Decision points (yes/no)
- **Ellipse**: Start/End points
- **Arrow**: Flow direction and relationships
- **Text**: Labels and annotations

### Layout Guidelines:
- **Vertical flow**: Top to bottom for main sequence
- **Horizontal branches**: Left/right for alternatives (Yes/No)
- **Dashed lines**: Secondary flows, loops, metadata
- **Rounded rectangles**: All process boxes use type 3 roundness
- **Grid alignment**: 10px grid for clean alignment

## Key Insights from Diagrams

### From 01_high_level_flow:
1. **Two-phase design**: Calculation (Dag Processor) vs Execution (Scheduler)
2. **Critical field**: `next_dagrun_create_after` is the bridge between phases
3. **Database-driven**: Scheduler makes decisions purely from database query

### From 02_scheduler_loop_detailed:
1. **Triple check**: Existence, max_active_runs, then create
2. **Continuous loop**: Runs approximately every 1 second
3. **Batch processing**: For each loop iteration, process multiple DAGs
4. **Update immediately**: After creating run, immediately calculate next one

## Relationships to Mermaid Diagrams

These Excalidraw diagrams correspond to Mermaid diagrams in `../dag_run_scheduling.md`:

| Excalidraw File | Mermaid Diagram |
|-----------------|----------------|
| 01_high_level_flow.excalidraw | Section: "High-Level Flow" (graph LR) |
| 02_scheduler_loop_detailed.excalidraw | Section: "Scheduling Loop" (flowchart TD) |

**Advantage of Excalidraw**:
- Hand-drawn aesthetic (easier to understand)
- Fully editable with drag-and-drop
- Can add annotations, highlights, and comments
- Better for presentations and workshops

**Advantage of Mermaid**:
- Version-controlled as text
- Auto-generated from code
- Renders inline in GitHub/GitLab
- Easier to maintain in documentation

## Creating More Diagrams

To add more diagrams to this collection:

1. **Start with Mermaid**: Write the diagram in Mermaid syntax first (in `../dag_run_scheduling.md`)
2. **Convert structure**: Map Mermaid elements to Excalidraw:
   - `graph` nodes → rectangles
   - `flowchart` diamonds → decision diamonds
   - `sequenceDiagram` → vertical lifelines
3. **Apply color scheme**: Use the colors above for consistency
4. **Add metadata**: Label with file number and topic
5. **Save with naming**: `NN_description.excalidraw`

## Examples to Add (Future)

Suggested additional diagrams:
- `03_timetable_decision_flow.excalidraw` - Catchup logic visualization
- `04_multi_scheduler_coordination.excalidraw` - Row locking sequence
- `05_asset_triggered_bug.excalidraw` - NULL ordering issue
- `06_database_schema_er.excalidraw` - DagModel ↔ DagRun relationship
- `07_timeline_gantt.excalidraw` - Time-based view of scheduling

## Technical Details

### File Format:
- **Type**: JSON
- **Version**: Excalidraw v2
- **Encoding**: UTF-8
- **Line Endings**: LF (Unix-style)

### Element Properties:
- **Position**: Absolute x,y coordinates
- **Size**: Width and height in pixels
- **Stroke**: Width 2-3px for emphasis
- **Roughness**: Level 1 (hand-drawn feel)
- **Opacity**: 100% (fully opaque)

### Compatibility:
- Compatible with Excalidraw web app (https://excalidraw.com)
- Compatible with Excalidraw VS Code extension
- Compatible with Excalidraw CLI tools
- Can be converted to/from Mermaid using `@excalidraw/mermaid-to-excalidraw`

## Resources

- **Excalidraw**: https://excalidraw.com
- **Documentation**: https://docs.excalidraw.com
- **Mermaid to Excalidraw API**: https://docs.excalidraw.com/docs/@excalidraw/mermaid-to-excalidraw/api
- **GitHub**: https://github.com/excalidraw/excalidraw

## Contributing

When adding or modifying diagrams:
1. Maintain the color scheme for consistency
2. Use the 10px grid for alignment
3. Keep text sizes consistent (16-20px for main text, 28-32px for titles)
4. Add diagram to this README with description
5. Cross-reference to corresponding Mermaid diagram
6. Export a PNG preview if possible (for quick reference)

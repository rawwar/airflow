# Scheduler Diagrams: Complete Overview

This document provides a comprehensive overview of all visualization formats available for understanding Airflow's scheduler behavior.

## Available Formats

### 1. Mermaid Diagrams (In dag_run_scheduling.md)

**File**: `dag_run_scheduling.md`

**Format**: Text-based, renders in GitHub/GitLab/VS Code

**Total**: 11 diagrams

**Diagrams**:
1. High-level flow (graph LR)
2. Complete scheduling flow (sequence diagram)
3. Timetable decision flow (flowchart TD)
4. DagModel calculation flow (flowchart TD)
5. Scheduler loop flow (flowchart TD)
6. Timeline Gantt chart (gantt)
7. Scheduler downtime scenario (flowchart TD)
8. Multi-scheduler coordination (sequence diagram)
9. Asset-triggered DAG bug (flowchart TD)
10. Entity-relationship diagram (erDiagram)
11. Summary visualization (graph TB)

**Advantages**:
- Version-controlled as text
- Auto-renders in documentation
- Easy to update
- No external tools needed

### 2. Excalidraw Diagrams (In excalidraw/ directory)

**Directory**: `excalidraw/`

**Format**: JSON (editable at https://excalidraw.com)

**Total**: 3 detailed diagrams

**Diagrams**:
1. `01_high_level_flow.excalidraw` (879 lines)
   - 5 main components with color coding
   - Shows critical field flow
   - Hand-drawn aesthetic

2. `02_scheduler_loop_detailed.excalidraw` (813 lines)
   - Complete loop with all decision points
   - 15+ elements including diamonds, boxes, arrows
   - Shows skip paths and loop continuation

3. `03_critical_decision_point.excalidraw` (564 lines)
   - Two-phase visualization
   - SQL query highlighted
   - Summary annotations

**Advantages**:
- Hand-drawn, approachable aesthetic
- Fully editable with drag-and-drop
- Great for presentations
- Can export to PNG/SVG

## Diagram Comparison Matrix

| Feature | Mermaid | Excalidraw |
|---------|---------|------------|
| **Format** | Text | JSON |
| **Editability** | Text editor | Graphical |
| **Version Control** | Excellent | Good |
| **Rendering** | Auto (GitHub/GitLab) | Manual |
| **Aesthetics** | Clean, technical | Hand-drawn, friendly |
| **Export** | PNG via tools | PNG/SVG built-in |
| **Learning Curve** | Low (syntax) | Very Low (drag-drop) |
| **Collaboration** | Git merges | File replacement |
| **Best For** | Documentation | Presentations |

## Coverage Map

### Core Concepts Covered:

```
┌───────────────────────────────────────────┐
│ Component            │ Mermaid │ Excalidraw │
├──────────────────────┼─────────┼────────────┤
│ High-level Flow      │    ✓    │     ✓      │
│ Dag Processor        │    ✓    │     ✓      │
│ Timetable Logic      │    ✓    │     ✓      │
│ DagModel Fields      │    ✓    │     ✓      │
│ Scheduler Loop       │    ✓    │     ✓      │
│ SQL Query            │    ✓    │     ✓      │
│ Critical Decision    │    ✓    │     ✓      │
│ Multi-Scheduler      │    ✓    │     -      │
│ Timeline/Gantt       │    ✓    │     -      │
│ Database Schema      │    ✓    │     -      │
│ Bug Visualization    │    ✓    │     -      │
└──────────────────────┴─────────┴────────────┘
```

## Color Scheme (Consistent Across All Diagrams)

### Component Colors:
- **Cyan (#4ecdc4)**: Dag Processor operations
- **Yellow (#ffd93d)**: DagModel table / Critical field
- **Light Green (#95e1d3)**: Scheduler operations  
- **Green (#b2f2bb)**: Success / Creation actions
- **Light Blue (#d0ebff)**: Iterative / Loop elements
- **Red (#ffe3e3)**: Critical decisions / Conditions
- **Orange (#ffec99)**: Key field calculations
- **Gray (#e9ecef)**: Skip / No-op actions

### Arrow Colors:
- **Black**: Main flow
- **Orange (dashed)**: Critical field flow
- **Red**: Critical decision flow
- **Green**: Success path
- **Blue (dashed)**: Loop / Iteration
- **Gray (dashed)**: Skip / Alternative path

## Usage Recommendations

### For Documentation:
✓ Use Mermaid diagrams
- Inline rendering in markdown
- Easy to update with code reviews
- Version control friendly

### For Presentations:
✓ Use Excalidraw diagrams
- Export to PNG/SVG
- Hand-drawn aesthetic is more engaging
- Easy to annotate during live demos

### For Learning:
✓ Start with Mermaid in documentation
✓ Use Excalidraw for interactive exploration
- Edit and experiment with flows
- Add your own annotations
- Customize colors for emphasis

## File Structure

```
files/docs/scheduler/
├── README.md                           # Quick reference
├── DIAGRAMS_OVERVIEW.md                # This file
├── dag_run_scheduling.md               # Main doc with Mermaid (633 lines)
└── excalidraw/
    ├── README.md                       # Excalidraw usage guide (198 lines)
    ├── 01_high_level_flow.excalidraw   # 879 lines
    ├── 02_scheduler_loop_detailed.excalidraw  # 813 lines
    └── 03_critical_decision_point.excalidraw  # 564 lines
```

## Statistics

- **Total Mermaid Diagrams**: 11
- **Total Excalidraw Diagrams**: 3
- **Total Lines of Mermaid Code**: ~300 lines (embedded in markdown)
- **Total Lines of Excalidraw JSON**: 2,256 lines
- **Documentation**: 1,029 lines (main doc + READMEs)
- **Total Visualization Content**: ~3,585 lines

## Key Insights Visualized

### 1. Two-Phase Design
**Covered in**: All diagrams
- Phase 1: Dag Processor calculates
- Phase 2: Scheduler executes
- Link: `next_dagrun_create_after` field

### 2. Critical Decision
**Covered in**: Mermaid #1, #5, #11 + Excalidraw #3
- SQL: `WHERE next_dagrun_create_after <= NOW()`
- This single comparison determines everything

### 3. Scheduler Loop
**Covered in**: Mermaid #5 + Excalidraw #2
- Runs every ~1 second
- Processes up to 10 DAGs per loop
- Three checks before creating run

### 4. Multi-Scheduler Safety
**Covered in**: Mermaid #8
- Row-level locking
- SKIP LOCKED prevents duplicates
- Each scheduler processes different DAGs

### 5. Bug: Asset DAG Ordering
**Covered in**: Mermaid #9
- NULL `next_dagrun_create_after` for asset-only DAGs
- Database-dependent NULL ordering
- Can cause starvation in high-load scenarios

## Quick Start Guide

### To View All Diagrams:

1. **Open documentation**:
   ```bash
   cat files/docs/scheduler/dag_run_scheduling.md
   ```
   Or view on GitHub (Mermaid auto-renders)

2. **Open Excalidraw diagram**:
   - Visit https://excalidraw.com
   - File → Open
   - Select any `.excalidraw` file

### To Edit Mermaid:

1. Edit the markdown file directly
2. Change text inside ` ```mermaid ... ``` ` blocks
3. Preview in VS Code with Mermaid extension
4. Or use https://mermaid.live

### To Edit Excalidraw:

1. Open file at https://excalidraw.com
2. Drag elements to rearrange
3. Double-click text to edit
4. Change colors via element properties
5. File → Save (downloads updated JSON)

## Converting Between Formats

### Mermaid to Excalidraw:

Use `@excalidraw/mermaid-to-excalidraw` package:

```bash
npm install @excalidraw/mermaid-to-excalidraw
```

```javascript
import { parseMermaidToExcalidraw } from "@excalidraw/mermaid-to-excalidraw";

const mermaidDefinition = `graph TD
  A[Start] --> B[Process]
  B --> C[End]`;

const { elements, files } = await parseMermaidToExcalidraw(mermaidDefinition);
// Save as .excalidraw file
```

### Excalidraw to PNG/SVG:

1. Open in Excalidraw
2. Select all (Ctrl+A)
3. Export Image → PNG or SVG
4. Choose resolution and background

## Future Additions

Suggested diagrams to add:

### Mermaid (in dag_run_scheduling.md):
- [ ] DAG pause/unpause flow
- [ ] Backfill vs scheduled run differences
- [ ] Task instance scheduling (next level down)

### Excalidraw:
- [ ] `04_timetable_catchup_logic.excalidraw` - Detailed catchup decisions
- [ ] `05_multi_scheduler_locking.excalidraw` - Database lock visualization
- [ ] `06_asset_dag_bug_detailed.excalidraw` - Bug with code examples

## Resources

- **Mermaid**: https://mermaid.js.org/
- **Mermaid Live Editor**: https://mermaid.live
- **Excalidraw**: https://excalidraw.com
- **Excalidraw Docs**: https://docs.excalidraw.com
- **Conversion API**: https://docs.excalidraw.com/docs/@excalidraw/mermaid-to-excalidraw/api

## Feedback & Contributions

When adding or modifying diagrams:

1. **Maintain color scheme** for consistency
2. **Cross-reference** between Mermaid and Excalidraw versions
3. **Update this overview** when adding new diagrams
4. **Test rendering** before committing:
   - Mermaid: Check in GitHub preview or mermaid.live
   - Excalidraw: Open and verify all elements visible
5. **Add explanations** in nearby markdown text
6. **Keep it simple**: One concept per diagram when possible

---

**Last Updated**: 2024-11-22  
**Total Diagrams**: 14 (11 Mermaid + 3 Excalidraw)  
**Coverage**: Complete scheduler flow from DAG file to DAG run

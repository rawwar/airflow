# Excalidraw Diagrams for Deferrable Tasks

Editable visual diagrams for understanding deferrable task execution in Apache Airflow.

## Files

### 1. Complete Deferrable Flow (`01_complete_deferrable_flow.excalidraw`)

**Purpose**: End-to-end execution flow showing all three phases

**Shows**:
- Phase 1: Task defers (Worker → Database)
- Phase 2: Triggerer monitors (Database → Triggerer)
- Phase 3: Trigger fires & task resumes (Triggerer → Database → Worker)
- Worker freed during DEFERRED state
- Async monitoring in triggerer

**Key Insight**: Worker is freed for 90% of the wait time!

### 2. Trigger Table Lifecycle (`02_trigger_table_lifecycle.excalidraw`)

**Purpose**: Database operations on the trigger table

**Shows**:
- INSERT: Worker creates trigger when task defers
- UPDATE: Triggerer claims trigger (sets triggerer_id)
- DELETE: Trigger removed after firing
- Encryption: kwargs encrypted with Fernet

**Key SQL Operations**:
```sql
INSERT INTO trigger (classpath, kwargs, created_date)
UPDATE trigger SET triggerer_id = X WHERE id = Y
DELETE FROM trigger WHERE id = Z
```

### 3. Triggerer Architecture (`03_triggerer_architecture.excalidraw`)

**Purpose**: Internal structure of the triggerer process

**Shows**:
- Main Thread: Heartbeat, DB polling, cleanup, capacity management
- Async Thread: Event loop running 1000+ triggers concurrently
- Database communication patterns
- Process separation (main vs async)

**Key Concept**: All triggers run in ONE async event loop!

### 4. State Machine (`04_state_machine.excalidraw`)

**Purpose**: Task instance state transitions with defer/resume

**Shows**:
- SCHEDULED → RUNNING: Worker starts
- RUNNING → DEFERRED: Task calls defer() (worker freed)
- DEFERRED → SCHEDULED: Trigger fires
- SCHEDULED → RUNNING: Worker resumes with callback
- RUNNING → SUCCESS: Task completes
- DEFERRED → FAILED: Trigger timeout or exception
- Re-defer path (condition not met)

**Key States**:
- **DEFERRED**: Worker freed, trigger_id set, monitored by triggerer
- **SCHEDULED**: Ready to resume, next_kwargs contains event payload

### 5. Debugging Flowchart (`05_debugging_deferrable.excalidraw`)

**Purpose**: Decision tree for troubleshooting stuck tasks

**Shows**:
- Problem: Task stuck in DEFERRED
- Decision 1: Trigger exists in DB?
  - No → Check triggerer logs for failure
  - Yes → Continue
- Decision 2: Triggerer assigned (triggerer_id)?
  - No → Check if triggerer running
  - Yes → Continue
- Decision 3: Triggerer alive (heartbeat)?
  - No → Wait ~5 min for orphan reclaim
  - Yes → Check logs for trigger errors

**Quick Actions**:
- Start triggerer: `airflow triggerer`
- Check heartbeat: `SELECT * FROM job WHERE job_type='TriggererJob'`
- Check logs: `tail -f logs/triggerer/<date>/triggerer.log`

## How to Use

### Viewing

1. **Online**: Open https://excalidraw.com
2. **File → Open**: Select any `.excalidraw` file
3. **View**: Pan (drag), zoom (scroll)

### Editing

1. **Open in Excalidraw**: File → Open
2. **Edit**: Click elements to select, drag to move
3. **Add**: Use toolbar (rectangle, arrow, text, etc.)
4. **Save**: File → Save to disk
5. **Export**: File → Export image (PNG/SVG)

### Integration

**Embed in docs**:
```markdown
![Deferrable Flow](excalidraw/01_complete_deferrable_flow.png)
```

**Export as PNG**:
1. Open in Excalidraw
2. File → Export image → PNG
3. Save to same directory

## Color Scheme

**Consistent across all diagrams**:

- **Cyan (#4ecdc4)**: Triggerer/Scheduler operations
- **Yellow (#ffd93d)**: Database/Queues/Storage
- **Green (#95e1d3, #b2f2bb)**: Success states, workers, completed actions
- **Red (#ffe3e3, #e03131)**: Error states, failures, problems
- **Orange (#ffec99, #f08c00)**: DEFERRED state, intermediate states, warnings
- **Blue (#d0ebff, #1971c2)**: Async operations, event loops, monitoring
- **Gray (#f8f9fa, #868e96)**: Containers, backgrounds, notes

## Diagram Guidelines

**When to use each diagram**:

- **01_complete_flow**: Explaining overall concept to new users
- **02_trigger_table**: Database-level debugging, SQL query understanding
- **03_triggerer_architecture**: Performance tuning, capacity planning
- **04_state_machine**: State transition bugs, resume failures
- **05_debugging**: Active troubleshooting sessions

**Best practices**:
- Show diagrams in order (01 → 05) for complete understanding
- Use debugging flowchart as quick reference during incidents
- Reference architecture diagram when discussing capacity/scaling

## Related Documentation

- Main docs: `../deferrable_task_lifecycle.md`
- README: `../README.md`
- Mermaid diagrams: Embedded in main documentation

## File Format

All files are JSON-based `.excalidraw` format:
- **Portable**: Open on any device with Excalidraw
- **Version-controllable**: Git-friendly text format
- **Editable**: Full editing capabilities preserved

**Structure**:
```json
{
  "type": "excalidraw",
  "version": 2,
  "elements": [...],  // All shapes, text, arrows
  "appState": {...},  // View settings
  "files": {}         // Embedded images
}
```

## Tips

**For presentations**:
1. Export all diagrams as PNG (high DPI)
2. Use diagrams 01 and 04 for overview slides
3. Use diagram 05 for troubleshooting workshops

**For documentation**:
1. Keep diagrams simple (< 20 elements)
2. Use consistent colors (see Color Scheme above)
3. Add labels to all arrows
4. Group related elements

**For debugging**:
1. Print diagram 05 (debugging flowchart)
2. Keep handy during incident response
3. Follow decision tree systematically

## Feedback

For improvements or corrections, update the diagrams and documentation together to maintain consistency.

# Topic Name (e.g., Core DAG Concepts)

## Topic Overview

Brief description of what this topic covers and why it's important for Airflow users.
This should be 2-3 sentences explaining the scope and purpose.

## Research & Background

### Key Concepts
- List important concepts that need to be understood
- Include links to official Airflow documentation
- Reference relevant Apache Airflow GitHub issues or PRs if applicable

### Common Use Cases
- Describe typical scenarios where these features are used
- Explain real-world applications

### Prerequisites
- What users should know before working with this topic
- Required Airflow version or dependencies
- Related topics that should be understood first

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. [Specific skill or understanding]
2. [Another specific skill or understanding]
3. [etc.]

---

# Subtopic 1: [Name]

## Overview
Description of this specific subtopic (1-2 sentences).

## Research Notes

### Documentation References
- [Airflow Docs - Relevant Section](https://airflow.apache.org/docs/...)
- [Related Tutorial](https://example.com)

### Important Details
- Key implementation details that DAG creators should know
- Common pitfalls or gotchas
- Best practices specific to this subtopic

### Technical Specifications
- API details, parameters, configuration options
- Version compatibility notes
- Performance considerations

## Tasks

### - [ ] X.Y.1 Descriptive Task Name (e.g., "DAG with Context Manager")
Filename: `01_01_01_descriptive_name.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Specific feature or pattern to demonstrate
- [ ] Edge case or error scenario to include
- [ ] Documentation or comments to add
- [ ] Another implementation requirement
- [ ] Ensure comprehensive docstring

---

### - [ ] X.Y.2 Another Descriptive Task Name
Filename: `01_01_02_another_name.py` | Tags: `['reference', 'category', 'level', 'type']`

- [ ] Implementation requirement 1
- [ ] Implementation requirement 2
- [ ] Add test coverage for edge case

---

# Subtopic 2: [Name]

## Overview
[Description of subtopic 2]

## Research Notes

### Documentation References
- [Links to docs]

### Important Details
- [Key points]

## Tasks

### - [ ] X.Y.Z Task Title

[Follow same format as above]

---

# Summary & Next Steps

## Topic Completion Checklist
- [ ] All subtasks have clear purpose and requirements
- [ ] Documentation references are included and valid
- [ ] Testing approach is defined for each task
- [ ] Tasks are ordered logically (beginner → advanced)
- [ ] Related tasks are cross-referenced

## Related Topics
List other plan sections that are related or build upon this topic:
- Section X: [Topic name and how it relates]
- Section Y: [Topic name and how it relates]

## Additional Resources
- [Blog posts, tutorials, or community resources]
- [Relevant GitHub discussions]
- [Stack Overflow common questions]

## Notes for Implementation
- Any general notes or reminders for when implementing these DAGs
- Common patterns that should be reused across tasks
- Specific testing environments or setups needed

---

## Template Notes

### Task Numbering Convention
- `X` = Section number (1-50)
- `Y` = Subtopic number within section (1-N)
- `Z` = Task number within subtopic (1-N)
- Example: `1.2.3` = Section 1, Subtopic 2, Task 3

### Tag Categories
**Level**: `beginner`, `intermediate`, `advanced`
**Category**: `core`, `providers`, `patterns`, `testing`, `observability`, etc.
**Type**: `success` (works as expected), `failure` (intentional error), `edge-case`, `anti-pattern`

### Filename Convention
Format: `<section>_<subtopic>_<task>_<descriptive_name>.py`
Example: `01_02_03_dag_with_timedelta_schedule.py`

### DAG File Structure
Each DAG file should include:
1. Module-level docstring with:
   - Section/Topic/Subtask identification
   - Purpose and learning objectives
   - Key features demonstrated
   - Expected behavior
   - References to documentation
2. Imports
3. DAG configuration
4. Task definitions
5. Task dependencies
6. Optional: Helper functions with docstrings

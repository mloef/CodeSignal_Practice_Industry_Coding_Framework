# Level 3: Task Prioritization and Sorting

## Objective
Enrich tasks with a prioritization attribute and implement sorting functionality in the TaskManager.

## Requirements

### Task Class Modifications
- Add a new attribute for `priority` with possible values: "low", "medium", or "high".
- Define a reasonable default if the priority is not provided.

### Task Sorting in TaskManager
- Implement methods to retrieve tasks sorted by priority.
  - Consider mapping each priority level to a numerical value (e.g., high: 3, medium: 2, low: 1) to ensure correct ordering.
- Implement methods to retrieve tasks sorted by creation time (implying that tasks are tracked with a timestamp or insertion order).

### Edge Cases and Traps
- Avoid simple string comparison for priority sorting which might lead to incorrect order.
- Ensure stable sorting when multiple tasks have the same priority by applying secondary criteria (like creation time).

## Design Considerations
- Focus on using Python's built-in sorting frameworks effectively.
- Ensure that the design is extendable and that additional sorting or filtering criteria can be integrated in the future. 
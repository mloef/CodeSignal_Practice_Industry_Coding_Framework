# Level 4: Task Filtering and Reporting

## Objective
Integrate filtering capabilities and generate summary reports for a comprehensive overview of all tasks.

## Requirements

### Filtering Functionality
- Implement methods in TaskManager to filter tasks based on various criteria:
  - Priority (e.g., filter only "high" priority tasks).
  - (Optionally) Status, such as pending vs. completed if such an attribute is added in future iterations.
- Ensure that filters can be combined (e.g., filtering tasks that are high priority and pending).

### Reporting
- Implement methods to generate summary statistics, including:
  - Total number of tasks.
  - Count of tasks grouped by priority (e.g., how many tasks are high, medium, low).
  - (Optionally) Count of tasks by status (if a status attribute is present).
- Provide a well-structured output, such as a dictionary or formatted string, that clearly presents these statistics.

## Design Considerations
- Avoid ad-hoc implementations by clearly separating filtering logic from reporting logic.
- Ensure the design is scalable to incorporate additional filters or report metrics in the future.
- Encourage thoughtful design to prevent inefficient implementations (e.g., multiple unoptimized passes over tasks). 
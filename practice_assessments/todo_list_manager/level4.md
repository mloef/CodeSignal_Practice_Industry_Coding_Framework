# Scenario

Your task is to extend the to-do list manager with task filtering and reporting capabilities. All operations described below should be implemented in the provided `solution.py` file.

## Level 4 – Task Filtering and Reporting

### Operations

- **FILTER_TASKS_BY_PRIORITY(priority)**
  - **Purpose:** Return a list of tasks that match the specified priority.
  - **Requirements:**
    - The `priority` parameter must be one of `"low"`, `"medium"`, or `"high"`.
    - Return a string formatted as a list containing the titles of the tasks with the specified priority, e.g., `"[Task A, Task B]"`.
    - If no tasks match the specified priority, return `"[]"`.

- **GENERATE_SUMMARY_REPORT()**
  - **Purpose:** Generate a summary report of the current tasks.
  - **Requirements:**
    - The report must include:
      - The total number of tasks.
      - A count of tasks grouped by each priority: `"high"`, `"medium"`, and `"low"`.
    - Return the report in a structured format. For example, a JSON-formatted string:
      ```
      {"total": 3, "high": 1, "medium": 1, "low": 1}
      ```
    - Ensure that the keys in the report are exactly `"total"`, `"high"`, `"medium"`, and `"low"`.

### Example

If there are three tasks in the system:
- One with priority `"high"`,
- One with priority `"medium"`,
- One with priority `"low"`,

Then calling `GENERATE_SUMMARY_REPORT()` should return a report similar to:
```
{"total": 3, "high": 1, "medium": 1, "low": 1}
```
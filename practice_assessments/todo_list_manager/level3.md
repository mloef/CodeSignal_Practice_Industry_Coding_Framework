# Scenario

Your task is to enhance the to-do list manager by introducing task prioritization and sorting functionality. All operations described below should be implemented in the provided `solution.py` file. When adding tasks, you will now handle an optional priority value.

## Level 3 – Task Prioritization and Sorting

### Operations

- **ADD_TASK(title, description, [priority])**
  - **Purpose:** Create a new task with a title, description, and an optional priority.
  - **Requirements:**
    - `title` and `description` must be non-empty strings.
    - The `priority` parameter is optional; if not provided, default to `"medium"`.
    - Valid priority values are `"low"`, `"medium"`, and `"high"`. If an invalid value is provided, you may treat it as `"medium"`.
    - On success, assign the task a unique identifier and return `"task added: <title>"`.

- **LIST_TASKS_BY_PRIORITY()**
  - **Purpose:** Return a list of tasks sorted by their priority.
  - **Requirements:**
    - Tasks must be sorted in descending order of priority: `"high"` first, then `"medium"`, followed by `"low"`.
    - If two tasks share the same priority, they should be sorted by their creation time (earlier tasks come first).
    - The output should be formatted as a string representing a list of task titles, e.g., `"[Task A, Task B]"`.
    - If no tasks exist, return `"[]"`.

### Example

Suppose the following tasks are added:
1. `ADD_TASK("Task A", "Description A", "high")` returns:
   ```
   task added: Task A
   ```
2. `ADD_TASK("Task B", "Description B", "low")` returns:
   ```
   task added: Task B
   ```
3. `ADD_TASK("Task C", "Description C")` returns (default priority `"medium"`):
   ```
   task added: Task C
   ```

Then, calling `LIST_TASKS_BY_PRIORITY()` should return a list with tasks ordered by priority, for example:
```
[Task A, Task C, Task B]
```
(assuming "Task A" was added before "Task C").
# Level 4 – Priority, Completion, Due Dates, and Searching

In this final level, you combine multiple new features on top of the existing code. All prior methods (from Levels 1–3) must continue to work exactly as specified.

---

## 1. Adding Priority and Completion

### `set_priority(task_id, priority)`
- **Purpose**: Assign a priority to an existing task.
- **Valid Values**: `"low"`, `"medium"`, `"high"`.
- **Expected Behavior**:
  1. If no task exists for `task_id`, return:
     ```
     error: task not found
     ```
  2. If `priority` is not one of `"low"`, `"medium"`, `"high"`, you may return:
     ```
     error: invalid priority
     ```
  3. Otherwise, set the task’s priority and return:
     ```
     priority set: <task_id>
     ```

### `complete_task(task_id)`
- **Purpose**: Mark the task as completed.
- **Expected Behavior**:
  1. If no task exists for `task_id`, return:
     ```
     error: task not found
     ```
  2. Otherwise, mark it completed and return:
     ```
     task completed: <task_id>
     ```

### `list_incomplete_tasks()`
- **Purpose**: Return a list of titles for tasks that are *not* completed, in the order they were added.
- **Expected Behavior**:
  - A string such as `"[TaskA, TaskB]"`.
  - If none are incomplete, return `"[]"`.

---

## 2. Adding Due Dates

### Revised `add_task(title, description, [due_date])`
- **Purpose**: Optionally let the caller specify a `due_date` in `"YYYY-MM-DD"` format.
- **Behavior**:
  - If `due_date` is omitted or invalid, the task is considered to have no due date.
  - Return format is still:
    ```
    task added: <title>, id: <task_id>
    ```
  - You do **not** need to show the `due_date` in the return string.

### `list_overdue_tasks(reference_date)`
- **Purpose**: Return the titles of all tasks whose `due_date` is strictly before `reference_date`.
- **Expected Behavior**:
  - Compare each task’s `due_date` (if any) to `reference_date` (also `"YYYY-MM-DD"`).
  - Return a Python-style list of titles in the order they were added, e.g. `"[Title1, Title2]"`.
  - If no tasks are overdue, return `"[]"`.

---

## 3. Searching

### `search_tasks(keyword)`
- **Purpose**: Return tasks (by title) whose **title or description** contains `keyword` (case-insensitive).
- **Expected Behavior**:
  - If no tasks match, return `"[]"`.
  - Otherwise, return the matching titles in a Python-style list.

---

## Important Notes

- All features from Levels 1–3 must remain operational. You cannot remove or break older functions or change their specified return strings.
- Level 4 adds multiple new fields and concepts (priority, completion, due date, searching). A flexible internal design from previous levels will adapt more easily.
- The final solution must handle collisions, ID-based references, and partial references from older methods.

Congratulations on making it to the final level!
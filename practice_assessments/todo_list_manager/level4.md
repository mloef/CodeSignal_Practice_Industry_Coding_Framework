# Level 4 – Priority, Completion, Due Dates, and Searching

In this final level, you combine multiple new features on top of the existing code. All prior methods (from Levels 1–3) must continue to work exactly as specified.

---

## 1. Adding Completion

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

### Revised `add_task_by_id(title, description, [due_date])`
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
  - Compare each task's `due_date` (if any) to `reference_date` (also `"YYYY-MM-DD"`).
  - Return a Python-style list of titles in the order they were added, e.g. `"[Title1, Title2]"`.
  - If no tasks are overdue, return `"[]"`.

---

## 3. Searching

### `search_tasks(keyword)`
- **Purpose**: Return id tasks (by title) whose **title or description** contains `keyword` (case-insensitive).
- **Expected Behavior**:
  - If no tasks match, return `"[]"`.
  - Otherwise, return the matching titles in a Python-style list.

---

## 4. Adding Priority

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
  3. Otherwise, set the task's priority and return:
     ```
     priority set: <task_id>
     ```

### Modified `list_tasks([priority])`

**Purpose**
Return all task titles in the order they were added. If `priority` is provided, return only tasks with that priority.

**Expected Behavior**
- If `priority` is not one of `"low"`, `"medium"`, `"high"`, return:
  ```
  error: invalid priority
  ```
- If tasks exist for the given `priority`, return them in a Python-style list of titles, for example:
  ```
  [Buy milk, Call John]
  ```
- If no tasks exist for the given `priority`, return:
  ```
  []
  ```
- If `priority` is not provided, return all tasks in the order they were added.

**Example Usage**
```
list_tasks()
→ "[Buy milk, Call John]"
```

## 5. Modified `get_task_by_id(task_id)` and `get_task(title)`

**Purpose**  
Return the task's title and description for the task with the given `task_id` or `title`. In addition, if the task has a priority, completion status, and/or due date, include the priority, completion status, and/or due date in the return string.

**Updated Behavior**
1. If the task with the matching `task_id` or `title` exists:
   - If the task has a priority, completion status, and due date, return:
     ```
     <title>, <description>, completed: <completed>, priority: <priority>, due_date: <due_date>
     ```
   - Remove fields as appropriate for tasks with other combinations of priority, completion status, and due date.
2. If no such task exists, return:
   ```
   error: task not found
   ```

**Example Usage**
```
add_task("T1", "D1", "2025-01-01")   // Suppose this task is assigned id 1
set_priority(1, "low")
complete_task(1)
get_task_by_id(1)
→ "T1, D1, completed: True, priority: low, due_date: 2025-01-01"
```

---

Congratulations on making it to the final level!

---

## Boilerplate

You may copy the below framework code into your solution file.

```python
   def complete_task(self, task_id):
       pass
   
   def list_incomplete_tasks(self):
       pass
    
   def add_task_by_id(self, title, description, due_date=None):
       pass
   
   def list_overdue_tasks(self, reference_date):
       pass
    
   def search_tasks(self, keyword):
       pass
   
   def set_priority(self, task_id, priority):
       pass
   
   def list_tasks(self, priority=None):
       pass
   
   def get_task_by_id(self, task_id):
       pass
   
   def get_task(self, title):
       pass
```

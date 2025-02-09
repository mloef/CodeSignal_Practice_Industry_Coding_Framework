# Level 3 – Introducing IDs (While Keeping Title-Based Methods)

Level 3 adds **unique IDs** to your tasks for the first time. You must still keep all methods from Levels 1 and 2 fully functional, but now you must add ID-based add/update/delete methods.

---

## 1. `add_task_by_id(title, description)`

**New Expected Behavior**
1. If `title` or `description` is empty, raise a `ValueError` with the message:
   ```
   "Invalid task data: parameters must not be empty"
   ```
2. Otherwise, assign a unique integer ID. Then return:
   ```
   task added: <title>, id: <task_id>
   ```
   - `<title>` is the given title.
   - `<task_id>` is the integer ID assigned to the newly created task.

---

## 2. `update_task_by_id(task_id, new_title, new_description)`

**Purpose**
Update a task using its integer ID.

**Expected Behavior**
1. If  `new_title`, or `new_description` is empty, raise a `ValueError` with the message:
   ```
   "Invalid task data: parameters must not be empty"
   ```
2. If no task exists for `task_id`, raise a `KeyError` with the message:
   ```
   "Task not found"
   ```
3. Otherwise, update the task's title and description and return:
   ```
   task updated: <task_id>
   ```

---

## 3. `delete_task_by_id(task_id)`

**Purpose**
Delete a task using its integer ID.

**Expected Behavior**
1. If no task exists for `task_id`, raise a `KeyError` with the message:
   ```
   "Task not found"
   ```
2. Otherwise, remove that task and return:
   ```
   task deleted: <task_id>
   ```

---

## 4. `get_task_by_id(task_id)`

**Purpose**
Return the task's title and description for the task with the given `task_id`.

**Expected Behavior**
1. If a task with the matching `task_id` exists, return:
   ```
   <title>, <description>
   ```
2. If no such task exists, raise a `KeyError` with the message:
   ```
   "Task not found"
   ```

**Example Usage**
```
add_task("Buy milk", "Get 2% milk")  // Suppose this is assigned id 1
get_task_id(1)
→ "Buy milk, Get 2% milk"
```

---

## Important Notes

- You must not remove the existing title-based methods (`add_task(title, description)`, `update_task(title, new_title, new_description)`, `delete_task(title)`, and `get_task(title)`) from Levels 1 and 2. They must remain valid.
- Now that tasks have IDs, you must maintain **two** different ways to locate them:
  1. By **title** (Level 2 and `get_task` defined above).
  2. By **task_id** (new in Level 3 via `update_task_by_id`, `delete_task_by_id`, and `get_task_by_id`).

---

## Boilerplate

You may copy the below framework code into your solution file.

```python
   def add_task_by_id(self, title, description):
      pass
   
   def update_task_by_id(self, task_id, new_title, new_description):
      pass
   
   def delete_task_by_id(self, task_id):
      pass
   
   def get_task_by_id(self, task_id):
      pass
```

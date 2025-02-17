# Level 2 – Update and Delete

In this level, you will **extend** the functionality from Level 1. You must retain the exact behavior of `add_task(title, description)`, `list_tasks()`, and `get_task(title)`.

Now you must introduce:

1. `update_task(title, new_title, new_description)`
2. `delete_task(title)`

---

## 1. `update_task(title, new_title, new_description)`

**Purpose**
Update the first task whose current title is exactly `title`.

**Expected Behavior**
1. If `title`,`new_title`, or `new_description` is empty, raise a `ValueError` with the message:
   ```
   "Invalid task data: parameters must not be empty"
   ```
2. If no task with the specified `title` exists, raise a `KeyError` with the message:
   ```
   "Task not found"
   ```
3. Otherwise, update that task’s title and description, and return:
   ```
   task updated: <title>
   ```
   Here, `<title>` refers to the **old** title used to find the task.

**Handling Duplicates**
- If multiple tasks share the same title, only update the **first** match in the order they were added.
- When a task is updated, it is considered as having been deleted and re-added. This ordering is important for duplicate handling.

---

## 2. `delete_task(title)`

**Purpose**
Delete the first task whose title matches `title`.

**Expected Behavior**
1. If `title` is empty, raise a `ValueError` with the message:
   ```
   "Invalid task data: parameters must not be empty"
   ```
2. If no task with the specified `title` exists, raise a `KeyError` with the message:
   ```
   "Task not found"
   ```
3. Otherwise, remove that first matching task and return:
   ```
   task deleted: <title>
   ```
   (where `<title>` is the original title used to locate the task).

**Handling Duplicates**
- If multiple tasks share the same title, only delete the **first** match.

---

## Boilerplate

You may copy the below framework code into your solution file.

```python
   def update_task(self, title, new_title, new_description):
      pass
   
   def delete_task(self, title):
      pass
```

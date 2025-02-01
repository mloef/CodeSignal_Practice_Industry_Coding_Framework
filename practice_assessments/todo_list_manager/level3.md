# Level 3 – Introducing IDs (While Keeping Title-Based Methods)

Level 3 adds **unique IDs** to your tasks for the first time. You must still keep all methods from Levels 1 and 2 fully functional, but now with two major changes:

1. `add_task(title, description)` must change its return string to include the newly assigned ID.
2. You must add ID-based update/delete methods, while retaining the old title-based ones.

---

## 1. Revised `add_task(title, description)`

**New Expected Behavior**
1. If `title` or `description` is empty, return:
   ```
   error: invalid task data
   ```
2. Otherwise, assign a unique integer ID (e.g. `1` for the first task, `2` for the second, etc.). Then return:
   ```
   task added: <title>, id: <task_id>
   ```
   - `<title>` is the given title.
   - `<task_id>` is the integer ID assigned to the newly created task.

**Note**
- This **overrides** Level 1’s return value for `add_task`. If you are testing Level 3 directly, your code must produce the new format.
- If tasks existed before Level 3, they must also be given IDs retroactively so that all tasks have IDs.

---

## 2. `update_task_id(task_id, new_title, new_description)`

**Purpose**
Update a task using its integer ID.

**Expected Behavior**
1. If `new_title` or `new_description` is empty, return:
   ```
   error: invalid task data
   ```
2. If no task exists for `task_id`, return:
   ```
   error: task not found
   ```
3. Otherwise, update the task’s title/description and return:
   ```
   task updated: <task_id>
   ```

---

## 3. `delete_task_id(task_id)`

**Purpose**
Delete a task using its integer ID.

**Expected Behavior**
1. If no task exists for `task_id`, return:
   ```
   error: task not found
   ```
2. Otherwise, remove that task and return:
   ```
   task deleted: <task_id>
   ```

---

## Important Notes

- You must not remove the existing `update_task(title, new_title, new_description)` or `delete_task(title)` from Level 2. They must remain valid, referencing tasks by title.
- Now that tasks have IDs, you must maintain **two** different ways to locate them:
  1. By **title** (Level 2).
  2. By **task_id** (new in Level 3).
- The updated `add_task` output must match exactly: `"task added: <title>, id: <task_id>"`.
# Level 2 – Title-Based Update and Delete (Duplicates Possible)

In this level, you will **extend** the functionality from Level 1. You must retain the exact behavior of:

- `add_task(title, description)` (unchanged from Level 1; do not alter its return string or logic).
- `list_tasks()`

Now you must introduce:

1. `update_task(title, new_title, new_description)`
2. `delete_task(title)`

---

## 1. `update_task(title, new_title, new_description)`

**Purpose**
Update the first task whose current title is exactly `title`.

**Expected Behavior**
1. If `new_title` or `new_description` is empty, return:
   ```
   error: invalid task data
   ```
2. If no task with the specified `title` exists, return:
   ```
   error: task not found
   ```
3. Otherwise, update that task’s title and description, and return:
   ```
   task updated: <title>
   ```
   Here, `<title>` refers to the **old** title used to find the task.

**Handling Duplicates**
- If multiple tasks share the same title, only update the **first** match in the order they were added.

---

## 2. `delete_task(title)`

**Purpose**
Delete the first task whose title matches `title`.

**Expected Behavior**
1. If no task with the specified `title` exists, return:
   ```
   error: task not found
   ```
2. Otherwise, remove that first matching task and return:
   ```
   task deleted: <title>
   ```
   (where `<title>` is the original title used to locate the task).

**Handling Duplicates**
- If multiple tasks share the same title, only delete the **first** match.

---

## Important Notes

- You **may not** modify the existing `add_task` or `list_tasks` outputs. They must behave exactly as they did in Level 1.
- This level intentionally does **not** use IDs. Tasks are identified only by their title, which can lead to collisions.
- You are free to store tasks however you like, but you must handle the possibility that multiple tasks share the same title.
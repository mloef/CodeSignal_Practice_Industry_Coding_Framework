# Scenario

Your task is to extend the to-do list manager to support modifications on existing tasks. All methods described below should be implemented in the provided `solution.py` file.

## Level 2 – Updating and Deleting Tasks

### Operations

- **update_task(task_id, new_title, new_description)**
  - **Purpose:** Update an existing task's title and description.
  - **Requirements:**
    - The task is identified by its unique `task_id` (an integer).
    - Both `new_title` and `new_description` must be non-empty strings.
    - If the task with the given `task_id` does not exist, return `"error: task not found"`.
    - If either `new_title` or `new_description` is empty, return `"error: invalid task data"`.
    - On success, update the task's title and description, and return `"task updated: <task_id>"`.

- **delete_task(task_id)**
  - **Purpose:** Delete an existing task.
  - **Requirements:**
    - The task is identified by its unique `task_id`.
    - If the task with the given `task_id` does not exist, return `"error: task not found"`.
    - On success, remove the task from the list and return `"task deleted: <task_id>"`.

### Example

Assume a task with `task_id` 1 exists:
- Calling `update_task(1, "New Title", "New Description")` should return:
  ```
  task updated: 1
  ```
- Calling `delete_task(1)` should return:
  ```
  task deleted: 1
  ```
If a task with the provided `task_id` does not exist, the corresponding function should return the appropriate error message.
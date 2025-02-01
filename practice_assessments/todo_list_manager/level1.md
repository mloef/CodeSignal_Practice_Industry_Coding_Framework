# Scenario

Your task is to implement a simplified version of a to-do list manager. All methods described below should be implemented in the provided `solution.py` file.

## Level 1 – Basic Task Creation and Listing

### Operations

- **add_task(title, description)**
  - **Purpose:** Create a new task with a given title and description.
  - **Requirements:**
    - Both `title` and `description` must be non-empty strings.
    - If either `title` or `description` is empty, return the string: `"error: invalid task data"`.
    - On success, return the string: `"task added: <title>"` where `<title>` is the title of the task.

- **list_tasks()**
  - **Purpose:** Return a list of all tasks in the order they were added.
  - **Requirements:**
    - The list should include the titles of the tasks.
    - The output must be formatted exactly as a string representing a list, e.g., `"[Buy milk, Call John]"`.
    - If no tasks exist, return `"[]"`.

### Example

1. Calling `add_task("Buy milk", "Get 2% milk")` should return:
   ```
   task added: Buy milk
   ```
2. Calling `add_task("Call John", "Discuss the project")` should return:
   ```
   task added: Call John
   ```
3. After adding the tasks above, calling `list_tasks()` should return:
   ```
   [Buy milk, Call John]
   ```
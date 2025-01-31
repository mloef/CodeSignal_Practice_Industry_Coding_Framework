# Scenario

Your task is to implement a simplified version of a to-do list manager.
All operations that should be supported are listed below.

## Level 1 – Basic Task Creation & Listing

- **TASK_CREATE(title, description)**
  - Create a new task with the provided title and description.
  - Return "created <title>" on success.
  - If a task with the same title already exists, return "error: task already exists".

- **TASK_GET(title)**
  - Return "got <title>" if the task exists.
  - If the task doesn't exist, return "task not found".

- **TASK_COPY(source_title, new_title)**
  - Duplicate the source task under a new title.
  - Return "copied <source_title> to <new_title>" on success.
  - If the source task doesn't exist, return "error: source task not found".
  - If a task with the new title already exists, overwrite it.

## Objective
Implement the foundational classes to handle tasks.

## Requirements

### Task Class
- Must represent a single to-do task.
- Attributes:
  - `title` (string): The name/summary of the task.
  - `description` (string): Additional details about the task.
- (Optionally) Include an internal unique identifier for each task for future updates and deletions.

### TaskManager Class
- Responsible for managing a collection of tasks.
- Must include:
  - A method to add a new task.
  - A method to list all tasks.
- Edge Cases:
  - Validate that tasks have non-empty title and description.

## Design Considerations
- Ensure proper encapsulation and separation between data representation (Task) and management logic (TaskManager).
- Avoid pitfalls like exposing internal data structures directly. 
# Level 1: Basic Task Creation and Listing

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
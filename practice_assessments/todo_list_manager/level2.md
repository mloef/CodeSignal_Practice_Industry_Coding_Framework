# Scenario

Your task is to extend the to-do list manager with advanced data processing capabilities.

## Level 2 – Data Structures & Data Processing

- **TASK_SEARCH(prefix)**
  - Find the top 10 tasks whose titles start with the provided prefix.
  - Order the tasks by the length of their description in descending order, and in case of a tie, by the task title in descending order.
  - Return the result in the format: "found [task1, task2, ...]". If no tasks match, return "found []".

## Objective
Extend the basic task management functionality to allow efficient search and ordering based on task attributes.

## Requirements

### TaskManager Class Extensions
- Provide a method to update an existing task by its unique identifier. Updates may include a new title and/or description.
- Provide a method to delete a task by its unique identifier.

### Error Handling
- Handle cases where an update or delete is attempted on a task that does not exist.
- Provide clear feedback or error messages when an operation fails due to a missing task.

## Design Considerations
- Avoid naive implementations that do not validate the existence of a task before updating or deleting.
- Consider efficient ways to manage and identify tasks to maintain data consistency. 
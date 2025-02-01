# Level 2: Updating and Deleting Tasks

## Objective
Extend the system to support modifying existing tasks through updates and deletions.

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
import unittest
from solution import TaskManager


class Level1(unittest.TestCase):
    """
    Tests for Level 1 – Add and List
    This assumes add_task returns "task added: <title>" without IDs,
    and list_tasks returns titles only in a Python-style list string.
    """

    def setUp(self):
        self.mgr = TaskManager()

    def test_add_task_valid(self):
        """
        Test that add_task with valid non-empty title/description
        returns 'task added: <title>'
        """
        result = self.mgr.add_task("Task1", "Description1")
        # Level 1 spec expects exactly: "task added: Task1"
        self.assertEqual(result, "task added: Task1")

    def test_add_task_empty_title(self):
        """
        add_task with empty title should raise ValueError
        """
        with self.assertRaises(ValueError) as context:
            self.mgr.add_task("", "Some description")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_add_task_empty_description(self):
        """
        add_task with empty description should raise ValueError
        """
        with self.assertRaises(ValueError) as context:
            self.mgr.add_task("Title only", "")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_list_tasks_empty(self):
        """
        list_tasks with no tasks => "[]"
        """
        result = self.mgr.list_tasks()
        self.assertEqual(result, "[]")

    def test_list_tasks_nonempty(self):
        """
        list_tasks returns something like: "[Task1, Task2]"
        in the order of insertion
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task2", "Description2")

        result = self.mgr.list_tasks()
        self.assertEqual(result, "[Task1, Task2]")
    
    def test_list_tasks_singleton(self):
        """
        list_tasks returns something like: "[Task1]" for one task
        """
        self.mgr.add_task("Task1", "Description1")

        result = self.mgr.list_tasks()
        self.assertEqual(result, "[Task1]")

    def test_list_tasks_many(self):
        """
        list_tasks returns something like: "[Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10]"
        for many tasks
        in the order of insertion
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task2", "Description2")
        self.mgr.add_task("Task3", "Description3")
        self.mgr.add_task("Task4", "Description4")
        self.mgr.add_task("Task5", "Description5")
        self.mgr.add_task("Task6", "Description6")
        self.mgr.add_task("Task7", "Description7")
        self.mgr.add_task("Task8", "Description8")
        self.mgr.add_task("Task9", "Description9")
        self.mgr.add_task("Task10", "Description10")

        result = self.mgr.list_tasks()
        self.assertEqual(result, "[Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10]")

    def test_list_tasks_duplicate(self):
        """
        list_tasks returns something like: "[Task1, Task1]" for duplicate titles
        in the order of insertion
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task1", "Description2")
    
        result = self.mgr.list_tasks()
        self.assertEqual(result, "[Task1, Task1]")
    
    def test_list_tasks_many_duplicate(self):
        """
        list_tasks returns something like: "[Task1, Task1, Task2, Task2, Task1, Task1, Task1, Task2, Task2, Task2]"
        for many tasks with duplicate titles
        in the order of insertion
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task1", "Description2")
        self.mgr.add_task("Task2", "Description3")
        self.mgr.add_task("Task2", "Description4")
        self.mgr.add_task("Task1", "Description5")
        self.mgr.add_task("Task1", "Description6")
        self.mgr.add_task("Task1", "Description7")
        self.mgr.add_task("Task2", "Description8")
        self.mgr.add_task("Task2", "Description9")
        self.mgr.add_task("Task2", "Description10")

        result = self.mgr.list_tasks()
        self.assertEqual(result, "[Task1, Task1, Task2, Task2, Task1, Task1, Task1, Task2, Task2, Task2]")

    def test_get_task_found(self):
        """
        Test that get_task returns the title and description
        if the task exists.
        """
        self.mgr.add_task("Task1", "Description1")
        result = self.mgr.get_task("Task1")
        self.assertEqual(result, "Task1, Description1")

    def test_get_task_not_found(self):
        """
        Test that get_task raises KeyError if the task is not found.
        """
        self.mgr.add_task("Task1", "Description1")
        with self.assertRaises(KeyError) as context:
            self.mgr.get_task("Task2")
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_get_task_not_found_empty(self):
        """
        Test that get_task raises KeyError if there are no tasks.
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.get_task("Task1")
        self.assertEqual(str(context.exception), "'Task not found'")
    
    def test_get_task_empty_title(self):
        """
        get_task with empty title should raise ValueError
        """
        with self.assertRaises(ValueError) as context:
            self.mgr.get_task("")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_get_task_duplicate(self):
        """
        If multiple tasks have the same title, get_task should return
        the details of the first one.
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task1", "Description2")
        result = self.mgr.get_task("Task1")
        self.assertEqual(result, "Task1, Description1")

    def test_get_task_many(self):
        """
        If multiple tasks have the same title, get_task should return
        the details of the first one.
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task2", "Description2")
        self.mgr.add_task("Task3", "Description3")
        self.mgr.add_task("Task4", "Description4")
        self.mgr.add_task("Task5", "Description5")
        self.mgr.add_task("Task6", "Description6")
        self.mgr.add_task("Task7", "Description7")
        self.mgr.add_task("Task8", "Description8")
        self.mgr.add_task("Task9", "Description9")
        self.mgr.add_task("Task10", "Description10")

        result = self.mgr.get_task("Task5")
        self.assertEqual(result, "Task5, Description5")


class Level2(Level1):
    """
    Tests for Level 2 – Update and Delete.
    The original add_task and list_tasks from Level 1 must remain unchanged.
    We now add:
      - update_task(title, new_title, new_description)
      - delete_task(title)
    """

    def test_update_task_invalid_data(self):
        """
        If title, new_title, or new_description is empty should raise ValueError
        """
        self.mgr.add_task("Task1", "Description1")
        with self.assertRaises(ValueError) as context:
            self.mgr.update_task("", "Task2", "Description2")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

        with self.assertRaises(ValueError) as context:
            self.mgr.update_task("Task1", "", "Description2")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")
    
        with self.assertRaises(ValueError) as context:
            self.mgr.update_task("Task1", "Task2", "")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_update_task_not_found(self):
        """
        If the title is not found should raise KeyError
        """
        self.mgr.add_task("Task1", "Description1")
        with self.assertRaises(KeyError) as context:
            self.mgr.update_task("Task2", "Task3", "Description3")
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_update_task_success(self):
        """
        Successfully updating the first matched task => "task updated: <old_title>"
        """
        self.mgr.add_task("Task1", "Description1")
        self.mgr.add_task("Task1", "Description2")  # same title to test first-match
        result = self.mgr.update_task("Task1", "Task1_Updated", "Description1Updated")
        self.assertEqual(result, "task updated: Task1")

        self.assertEqual(self.mgr.list_tasks(), "[Task1, Task1_Updated]")
        # Only first match should have changed
        self.assertEqual(
            self.mgr.get_task("Task1_Updated"), "Task1_Updated, Description1Updated"
        )
        # The second one should remain unchanged
        self.assertEqual(self.mgr.get_task("Task1"), "Task1, Description2")

    def test_delete_task_invalid_data(self):
        """
         If title is empty should raise ValueError
        """
        with self.assertRaises(ValueError) as context:
            self.mgr.delete_task("")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_delete_task_not_found(self):
        """
        If no task with given title should raise KeyError
        """
        self.mgr.add_task("TaskA", "DescriptionA")
        with self.assertRaises(KeyError) as context:
            self.mgr.delete_task("TaskB")
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_delete_task_success(self):
        """
        If found => "task deleted: <title>", and only the first match is deleted.
        """
        self.mgr.add_task("TaskA", "DescA")
        self.mgr.add_task("TaskA", "DescB")
        self.mgr.add_task("TaskC", "DescC")

        result = self.mgr.delete_task("TaskA")
        self.assertEqual(result, "task deleted: TaskA")
        self.assertEqual(self.mgr.list_tasks(), "[TaskA, TaskC]")
        # The first TaskA was removed, second TaskA + TaskC remain

    def test_update_task_second_unchanged(self):
        """
        If multiple tasks share the same title, only the first is updated, leaving the second unchanged.
        """
        self.mgr.add_task("TaskA", "DescFirst")
        self.mgr.add_task("TaskA", "DescSecond")
        result = self.mgr.update_task("TaskA", "TaskA_updated", "DescUpdated")
        self.assertEqual(result, "task updated: TaskA")
        # The second remains with old data
        self.assertEqual(self.mgr.get_task("TaskA"), "TaskA, DescSecond")

    def test_delete_task_twice_duplicates(self):
        """
        If multiple tasks share the same title, delete_task should remove the first occurrence each time it's called.
        """
        self.mgr.add_task("TaskA", "Desc1")
        self.mgr.add_task("TaskA", "Desc2")
        self.mgr.add_task("TaskA", "Desc3")
        result = self.mgr.delete_task("TaskA")
        self.assertEqual(result, "task deleted: TaskA")
        self.assertEqual(self.mgr.list_tasks(), "[TaskA, TaskA]")

        # Deleting the same title again removes the next one
        result = self.mgr.delete_task("TaskA")
        self.assertEqual(result, "task deleted: TaskA")
        self.assertEqual(self.mgr.list_tasks(), "[TaskA]")

    def test_update_task_existing_title_duplication(self):
        """
        Updating a task's title to another existing title is allowed,
        and does not affect the tasks that already have that title.
        """
        self.mgr.add_task("TaskX", "DescX")
        self.mgr.add_task("TaskY", "DescY")
        result = self.mgr.update_task("TaskX", "TaskY", "DescUpdated")
        self.assertEqual(result, "task updated: TaskX")
        self.assertEqual(self.mgr.get_task("TaskY"), "TaskY, DescY")
        # The updated one is also now titled "TaskY". So we have two tasks titled "TaskY".
        all_tasks = self.mgr.list_tasks()
        self.assertEqual(all_tasks, "[TaskY, TaskY]")
        # The first is "TaskY, DescUpdated", the second is "TaskY, DescY"


class Level3(Level2):
    """
    Tests for Level 3 – Introducing IDs (while retaining title-based methods).
    The add_task behavior changes to => "task added: <title>, id: <task_id>"
    We also add:
      - update_task_by_id(task_id, new_title, new_description)
      - delete_task_by_id(task_id)
    """

    def parse_id(self, result):
        pieces = result.split("id: ")
        self.assertEqual(len(pieces), 2)
        task_id = int(pieces[1])
        return task_id

    def test_add_task_includes_id(self):
        """
        Now we expect add_task to return "task added: <title>, id: <task_id>"
        """
        result = self.mgr.add_task_by_id("Buy milk", "Get 2% milk")
        task_id = self.parse_id(result)
        self.assertEqual(result, f"task added: Buy milk, id: {task_id}")

        result = self.mgr.add_task_by_id("Call John", "Remind him about the meeting")
        task_id = self.parse_id(result)
        self.assertEqual(result, f"task added: Call John, id: {task_id}")

    def test_add_task_invalid_data(self):
        """
        If title or description is empty should raise ValueError
        """
        with self.assertRaises(ValueError) as context:
            self.mgr.add_task_by_id("", "No title")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

        with self.assertRaises(ValueError) as context:
            self.mgr.add_task_by_id("No desc", "")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_update_task_by_id_not_found(self):
        """
        If no task with given task_id should raise KeyError
        """
        task_id = self.parse_id(self.mgr.add_task_by_id("A", "B"))
        with self.assertRaises(KeyError) as context:
            self.mgr.update_task_by_id(task_id + 1, "Title", "Desc")
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_update_task_by_id_invalid_data(self):
        """
        If new_title or new_description is empty should raise ValueError
        """
        task_id = self.parse_id(self.mgr.add_task_by_id("Task1", "Desc1"))
        with self.assertRaises(ValueError) as context:
            self.mgr.update_task_by_id(task_id, "", "NewDesc")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

        with self.assertRaises(ValueError) as context:
            self.mgr.update_task_by_id(task_id, "NewTitle", "")
        self.assertEqual(str(context.exception), "Invalid task data: parameters must not be empty")

    def test_update_task_by_id_zero(self):
        """
        Handles zero id by throwing missing task
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.update_task_by_id(0, "NewTitle", "NewDesc")
        self.assertEqual(str(context.exception), "'Task not found'")
    
    def test_update_task_by_id_negative(self):
        """
        Handles negative id by throwing missing task
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.update_task_by_id(-1, "NewTitle", "NewDesc")
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_update_task_by_id_success(self):
        """
        update_task_by_id => "task updated: <task_id>"
        """
        self.mgr.add_task_by_id("Task1", "Desc1")
        task_id = self.parse_id(self.mgr.add_task_by_id("Task2", "Desc2"))

        result = self.mgr.update_task_by_id(task_id, "Task2_new", "Desc2_new")
        self.assertEqual(result, f"task updated: {task_id}")
        self.assertEqual(self.mgr.get_task_by_id(task_id), "Task2_new, Desc2_new")

    def test_delete_task_by_id_not_found(self):
        """
        If no task with the given ID should raise KeyError
        """
        task_id = self.parse_id(self.mgr.add_task_by_id("A", "B"))
        with self.assertRaises(KeyError) as context:
            self.mgr.delete_task_by_id(task_id + 1)
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_delete_task_by_id_zero(self):
        """
        Handles zero id by throwing missing task
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.delete_task_by_id(0)
        self.assertEqual(str(context.exception), "'Task not found'")
    
    def test_delete_task_by_id_negative(self):
        """
        Handles negative id by throwing missing task
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.delete_task_by_id(-1)
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_delete_task_by_id_success(self):
        """
        If found => "task deleted: <task_id>"
        """
        result = self.mgr.add_task_by_id("T1", "D1")
        task_id1 = self.parse_id(result)
        self.assertEqual(result, f"task added: T1, id: {task_id1}")
        result = self.mgr.add_task_by_id("T2", "D2")
        task_id2 = self.parse_id(result)
        self.assertEqual(result, f"task added: T2, id: {task_id2}")
        result = self.mgr.delete_task_by_id(task_id1)
        self.assertEqual(result, f"task deleted: {task_id1}")
        self.assertEqual(self.mgr.list_tasks(), "[T2]")
        self.assertEqual(self.mgr.get_task_by_id(task_id2), "T2, D2")

    def test_get_task_by_id_found(self):
        """
        Test that get_task_by_id returns the title and description when the task exists.
        """
        result = self.mgr.add_task_by_id("Buy milk", "Get 2% milk")  # Expected id: 1
        id_val = int(result.split("id: ")[1])
        result = self.mgr.get_task_by_id(id_val)
        self.assertEqual(result, "Buy milk, Get 2% milk")

    def test_get_task_by_id_not_found(self):
        """
        Test that get_task_by_id returns an error message when the task id does not exist.
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.get_task_by_id(999)
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_get_task_by_id_zero(self):
        """
        Handles zero id by throwing missing task
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.get_task_by_id(0)
        self.assertEqual(str(context.exception), "'Task not found'")
    
    def test_get_task_by_id_negative(self):
        """
        Handles negative id by throwing missing task
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.get_task_by_id(-1)
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_get_task_by_id_duplicate_titles(self):
        """
        Even if multiple tasks share the same title, get_task_by_id retrieves the task with the given id.
        """
        self.mgr.add_task_by_id("TaskA", "First description")
        task_id = self.parse_id(self.mgr.add_task_by_id("TaskA", "Second description"))
        result = self.mgr.get_task_by_id(task_id)
        self.assertEqual(result, "TaskA, Second description")

    def test_update_task_by_id_does_not_affect_title_updates(self):
        """
        Updating a task by ID should only change that specific task,
        even if multiple tasks share the same title.
        """
        task_id1 = self.parse_id(self.mgr.add_task_by_id("TaskX", "DescX"))
        task_id2 = self.parse_id(self.mgr.add_task_by_id("TaskX", "DescX2"))

        # Update the second one by ID
        result = self.mgr.update_task_by_id(task_id2, "TaskX_updated", "DescX2_updated")
        self.assertEqual(result, f"task updated: {task_id2}")

        # Confirm the first remains unchanged
        self.assertEqual(self.mgr.get_task_by_id(task_id1), "TaskX, DescX")

        # Confirm the second is changed
        self.assertEqual(self.mgr.get_task_by_id(task_id2), "TaskX_updated, DescX2_updated")

        # Title-based get_task("TaskX") should still return the first
        self.assertEqual(self.mgr.get_task("TaskX"), "TaskX, DescX")

        # Title-based get_task("TaskX_updated") should now return the second
        self.assertEqual(self.mgr.get_task("TaskX_updated"), "TaskX_updated, DescX2_updated")

    def test_delete_task_by_id_vs_delete_task_title(self):
        """
        Show that deleting by ID only removes the specified task,
        while delete_task(title) removes the first with that title.
        """
        self.mgr.add_task_by_id("TaskA", "Desc1")
        task_id = self.parse_id(self.mgr.add_task_by_id("TaskA", "Desc2"))
        self.mgr.add_task_by_id("TaskB", "DescB")

        # Deleting by id
        result = self.mgr.delete_task_by_id(task_id)
        self.assertEqual(result, f"task deleted: {task_id}")
        # So we should have TaskA(id1) and TaskB(id3) left
        all_titles = self.mgr.list_tasks()
        self.assertEqual(all_titles, "[TaskA, TaskB]")
        # TaskA should correspond to Desc1
        self.assertEqual(self.mgr.get_task("TaskA"), "TaskA, Desc1")

        # Deleting by title "TaskB"
        result = self.mgr.delete_task("TaskB")
        self.assertEqual(result, "task deleted: TaskB")
        # Now only TaskA remains
        all_titles = self.mgr.list_tasks()
        self.assertEqual(all_titles, "[TaskA]")

    # TODO: add more tests for mixing title and ID operations

class Level4(Level3):
    """
    Tests for Level 4 – Priority, Completion, Due Dates, Searching
    Adds:
      - set_priority(task_id, priority)
      - complete_task(task_id)
      - list_incomplete_tasks()
      - (Revised) add_task_by_id(title, desc, [due_date]) to store due date if valid
      - list_overdue_tasks(reference_date)
      - search_tasks(keyword)
      - (Revised) get_task_by_id optionally returns priority, completed, due_date
      - (Revised) list_tasks(priority=None) to filter by priority if provided
    """

    # TODO: add test cases for add_task with due_date
    # TODO: test update_task with metadata
    # TODO: check list_overdue_tasks with same date as due
    # TODO: check optional args with empty string/0 - falsy!

    def test_set_priority_errors(self):
        """
        - If no task should raise KeyError
        - If invalid priority should raise ValueError
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.set_priority(1, "high")
        self.assertEqual(str(context.exception), "'Task not found'")

        task_id = self.parse_id(self.mgr.add_task_by_id("T1", "D1"))
        with self.assertRaises(ValueError) as context:
            self.mgr.set_priority(task_id, "invalid")
        self.assertEqual(str(context.exception), "Invalid priority value")

    def test_set_priority_success(self):
        """
        set_priority => "priority set: <task_id>"
        and
        get_task_by_id should now include the priority in its return string.
        """
        task_id = self.parse_id(self.mgr.add_task_by_id("T1", "D1"))
        result = self.mgr.set_priority(task_id, "low")
        self.assertEqual(result, f"priority set: {task_id}")
        # Verify priority via get_task_by_id method
        task_details = self.mgr.get_task_by_id(task_id)
        self.assertEqual(task_details, f"T1, D1, priority: low")

    def test_complete_task_errors(self):
        """
        If no task should raise KeyError
        """
        with self.assertRaises(KeyError) as context:
            self.mgr.complete_task(1)
        self.assertEqual(str(context.exception), "'Task not found'")

    def test_complete_task_success(self):
        """
        complete_task => "task completed: <task_id>"
        sets completed = True and task is no longer in list_incomplete_tasks.
        """
        result = self.mgr.add_task_by_id("T1", "D1")
        task_id = int(result.split("id: ")[1])
        self.assertEqual(self.mgr.list_incomplete_tasks(), "[T1]")
        result = self.mgr.complete_task(task_id)
        self.assertEqual(result, f"task completed: {task_id}")
        self.assertEqual(self.mgr.list_incomplete_tasks(), "[]")

    def test_list_incomplete_tasks_none(self):
        """
        If all tasks are complete (or none exist), => "[]"
        """
        self.assertEqual(self.mgr.list_incomplete_tasks(), "[]")

        # Add tasks and complete them
        result = self.mgr.add_task_by_id("T1", "D1")  # id=1
        id1 = int(result.split("id: ")[1])
        result = self.mgr.add_task_by_id("T2", "D2")  # id=2
        id2 = int(result.split("id: ")[1])
        self.mgr.complete_task(id1)
        self.mgr.complete_task(id2)
        self.assertEqual(self.mgr.list_incomplete_tasks(), "[]")

    def test_list_incomplete_tasks_some(self):
        """
        Show only incomplete tasks in insertion order => "[Title1, Title2]"
        """
        self.mgr.add_task_by_id("Buy milk", "Get 2% milk")  # id=1
        result = self.mgr.add_task_by_id("Call John", "Remind him")  # id=2
        id2 = int(result.split("id: ")[1])
        result = self.mgr.add_task_by_id("Meeting notes", "Write up")  # id=3

        # Mark only the second task as complete.
        self.mgr.complete_task(id2)
        incomplete = self.mgr.list_incomplete_tasks()
        self.assertEqual(incomplete, "[Buy milk, Meeting notes]")

    def test_add_task_by_id_due_date(self):
        """
        We can supply a valid or invalid due_date to add_task_by_id.
        Only valid "YYYY-MM-DD" is stored; otherwise should raise ValueError.
        The return string is still "task added: <title>, id: <task_id>"
        """
        result1 = self.mgr.add_task_by_id("TaskWithDate", "Desc", "2025-12-31")
        task_id = self.parse_id(result1)
        self.assertEqual(result1, f"task added: TaskWithDate, id: {task_id}")
        self.assertEqual(self.mgr.list_overdue_tasks("9999-01-01"), "[TaskWithDate]")

        with self.assertRaises(ValueError) as context:
            self.mgr.add_task_by_id("TaskInvalidDate", "Desc", "invalid-date")
        self.assertEqual(str(context.exception), "Invalid date format. Use YYYY-MM-DD")

    def test_list_overdue_tasks_none(self):
        """
        If no tasks are overdue return "[]".
        If reference_date is invalid should raise ValueError.
        """
        # add tasks with valid due_dates
        self.mgr.add_task_by_id("Task1", "Desc1", "2025-12-31")  # id=1
        self.mgr.add_task_by_id("Task2", "Desc2", "2025-01-01")  # id=2
        
        # reference date invalid should raise ValueError
        with self.assertRaises(ValueError) as context:
            self.mgr.list_overdue_tasks("bad-date")
        self.assertEqual(str(context.exception), "Invalid date format. Use YYYY-MM-DD")

        # reference date = "2024-12-31" => no tasks before that
        self.assertEqual(self.mgr.list_overdue_tasks("2024-12-31"), "[]")

    def test_list_overdue_tasks_some(self):
        """
        If a task has due_date < reference_date => it's overdue
        """
        self.mgr.add_task_by_id("Task1", "Desc1", "2025-01-01")  # id=1
        self.mgr.add_task_by_id("Task2", "Desc2", "2024-12-31")  # id=2
        self.mgr.add_task_by_id("Task3", "Desc3")  # id=3, no due_date

        # Reference date "2025-01-01" means tasks strictly before that are overdue.
        overdue = self.mgr.list_overdue_tasks("2025-01-01")
        self.assertEqual(overdue, "[Task2]")

    def test_search_tasks_none(self):
        """
        If no tasks match => "[]"
        """
        self.mgr.add_task_by_id("Grocery List", "Buy apples and oranges")
        self.mgr.add_task_by_id("Work", "Email John about the report")
        result = self.mgr.search_tasks("meeting")
        self.assertEqual(result, "[]")

    def test_search_tasks_some(self):
        """
        search_tasks(keyword) => match in title or description, case-insensitive
        Return titles in insertion order in a Python-style list string
        """
        self.mgr.add_task_by_id("Grocery List", "Buy apples and oranges")  # id=1
        self.mgr.add_task_by_id("Meeting Prep", "Prepare slides and notes")  # id=2
        self.mgr.add_task_by_id("Work", "Email John about the meeting")  # id=3

        result1 = self.mgr.search_tasks("apple")
        self.assertEqual(result1, "[Grocery List]")

        result2 = self.mgr.search_tasks("MEETING")
        # Matches "Meeting Prep" (in title) and "meeting" in description of "Work"
        self.assertEqual(result2, "[Meeting Prep, Work]")
    
    def test_list_tasks_with_priority_filter(self):
        """
        If priority is specified, only tasks with that priority should be returned.
        If no tasks match that priority, return "[]".
        If the priority is invalid, should raise ValueError.
        If priority is None, return all tasks in insertion order.
        """
        task_id1 = self.parse_id(self.mgr.add_task_by_id("T1", "D1"))
        self.mgr.set_priority(task_id1, "low")

        task_id2 = self.parse_id(self.mgr.add_task_by_id("T2", "D2"))
        self.mgr.set_priority(task_id2, "medium")

        # Check filtering
        self.assertEqual(self.mgr.list_tasks("low"), "[T1]")
        self.assertEqual(self.mgr.list_tasks("medium"), "[T2]")
        self.assertEqual(self.mgr.list_tasks("high"), "[]")
        
        # Invalid priority should raise ValueError
        with self.assertRaises(ValueError) as context:
            self.mgr.list_tasks("invalid")
        self.assertEqual(str(context.exception), "Invalid priority value")

        # No priority => all tasks
        self.assertEqual(self.mgr.list_tasks(), "[T1, T2]")

    def test_get_task_includes_all_fields(self):
        """
        get_task_by_id or get_task should include completed, priority, due_date fields if present.
        """
        result = self.mgr.add_task_by_id("MultiField", "Full test", "2030-01-02")
        id_val = int(result.split("id: ")[1])

        # Mark complete
        self.mgr.complete_task(id_val)
        # Set priority
        self.mgr.set_priority(id_val, "high")

        # get_task_by_id
        info = self.mgr.get_task_by_id(id_val)
        self.assertEqual(info, "MultiField, Full test, completed: True, priority: high, due date: 2030-01-02")

        # get_task by title
        info2 = self.mgr.get_task("MultiField")
        self.assertEqual(info2, "MultiField, Full test, completed: True, priority: high, due date: 2030-01-02")


if __name__ == "__main__":
    unittest.main()

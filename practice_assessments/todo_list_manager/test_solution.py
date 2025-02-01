import unittest
from solution import TaskManager


class TestLevel1(unittest.TestCase):
    """
    Tests for Level 1 – Basic Add and List (no IDs, no updates/deletes).
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
        result = self.mgr.add_task("Buy milk", "Get 2% milk")
        # Level 1 spec expects exactly: "task added: Buy milk"
        self.assertEqual(result, "task added: Buy milk")

    def test_add_task_empty_title(self):
        """
        add_task with empty title => "error: invalid task data"
        """
        result = self.mgr.add_task("", "Some description")
        self.assertEqual(result, "error: invalid task data")

    def test_add_task_empty_description(self):
        """
        add_task with empty description => "error: invalid task data"
        """
        result = self.mgr.add_task("Title only", "")
        self.assertEqual(result, "error: invalid task data")

    def test_list_tasks_empty(self):
        """
        list_tasks with no tasks => "[]"
        """
        result = self.mgr.list_tasks()
        self.assertEqual(result, "[]")

    def test_list_tasks_nonempty(self):
        """
        list_tasks returns something like: "[Buy milk, Call John]"
        in the order of insertion
        """
        self.mgr.add_task("Buy milk", "Get 2% milk")
        self.mgr.add_task("Call John", "Reminder to call John")

        result = self.mgr.list_tasks()
        self.assertEqual(result, "[Buy milk, Call John]")


class TestLevel2(unittest.TestCase):
    """
    Tests for Level 2 – Title-Based Update and Delete (Duplicates possible).
    The original add_task and list_tasks from Level 1 must remain unchanged.
    We now add:
      - update_task(title, new_title, new_description)
      - delete_task(title)
    """

    def setUp(self):
        self.mgr = TaskManager()

    def test_update_task_invalid_data(self):
        """
        If new_title or new_description is empty => "error: invalid task data"
        """
        self.mgr.add_task("TaskA", "DescriptionA")  # "task added: TaskA"
        result = self.mgr.update_task("TaskA", "", "NewDesc")
        self.assertEqual(result, "error: invalid task data")

        result = self.mgr.update_task("TaskA", "NewTitle", "")
        self.assertEqual(result, "error: invalid task data")

    def test_update_task_not_found(self):
        """
        If the title is not found => "error: task not found"
        """
        self.mgr.add_task("TaskA", "DescriptionA")
        result = self.mgr.update_task("NonExisting", "NewTitle", "NewDesc")
        self.assertEqual(result, "error: task not found")

    def test_update_task_success(self):
        """
        Successfully updating the first matched task => "task updated: <old_title>"
        """
        self.mgr.add_task("TaskA", "DescriptionA")
        self.mgr.add_task("TaskA", "DescriptionDuplicate")  # same title to test first-match
        result = self.mgr.update_task("TaskA", "TaskA_Updated", "DescriptionUpdated")
        self.assertEqual(result, "task updated: TaskA")

        # Only first match should have changed
        self.assertEqual(self.mgr.tasks[0].title, "TaskA_Updated")
        self.assertEqual(self.mgr.tasks[0].description, "DescriptionUpdated")
        # The second one should remain unchanged
        self.assertEqual(self.mgr.tasks[1].title, "TaskA")
        self.assertEqual(self.mgr.tasks[1].description, "DescriptionDuplicate")

    def test_delete_task_not_found(self):
        """
        If no task with given title => "error: task not found"
        """
        self.mgr.add_task("TaskA", "DescriptionA")
        result = self.mgr.delete_task("TaskB")
        self.assertEqual(result, "error: task not found")

    def test_delete_task_success(self):
        """
        If found => "task deleted: <title>", and only the first match is deleted.
        """
        self.mgr.add_task("TaskA", "DescA")
        self.mgr.add_task("TaskA", "DescB")
        self.mgr.add_task("TaskC", "DescC")

        result = self.mgr.delete_task("TaskA")
        self.assertEqual(result, "task deleted: TaskA")
        self.assertEqual(len(self.mgr.tasks), 2)
        # The first TaskA was removed, second TaskA + TaskC remain
        self.assertEqual(self.mgr.tasks[0].title, "TaskA")
        self.assertEqual(self.mgr.tasks[1].title, "TaskC")

    def test_list_tasks_unchanged_behavior(self):
        """
        Ensure add_task + list_tasks from Level 1 still behave the same.
        """
        self.mgr.add_task("Buy milk", "Get 2% milk")
        self.mgr.add_task("Call John", "Ring him at 5pm")

        self.assertEqual(self.mgr.list_tasks(), "[Buy milk, Call John]")


class TestLevel3(unittest.TestCase):
    """
    Tests for Level 3 – Introducing IDs (while retaining title-based methods).
    The add_task behavior changes to => "task added: <title>, id: <task_id>"
    We also add:
      - update_task_id(task_id, new_title, new_description)
      - delete_task_id(task_id)
    """

    def setUp(self):
        self.mgr = TaskManager()

    def test_add_task_includes_id(self):
        """
        Now we expect add_task to return "task added: <title>, id: <task_id>"
        """
        result = self.mgr.add_task("Buy milk", "Get 2% milk")
        self.assertEqual(result, "task added: Buy milk, id: 1")

        result = self.mgr.add_task("Call John", "Remind him about the meeting")
        self.assertEqual(result, "task added: Call John, id: 2")

    def test_add_task_invalid_data(self):
        """
        If title or description is empty => "error: invalid task data"
        """
        result = self.mgr.add_task("", "No title")
        self.assertEqual(result, "error: invalid task data")

        result = self.mgr.add_task("No desc", "")
        self.assertEqual(result, "error: invalid task data")

    def test_update_task_id_not_found(self):
        """
        If no task with given task_id => "error: task not found"
        """
        # create a task so next_id is at least 2
        self.mgr.add_task("A", "B")
        result = self.mgr.update_task_id(999, "Title", "Desc")
        self.assertEqual(result, "error: task not found")

    def test_update_task_id_invalid_data(self):
        """
        If new_title or new_description is empty => "error: invalid task data"
        """
        self.mgr.add_task("Task1", "Desc1")  # id 1
        result = self.mgr.update_task_id(1, "", "NewDesc")
        self.assertEqual(result, "error: invalid task data")

        result = self.mgr.update_task_id(1, "NewTitle", "")
        self.assertEqual(result, "error: invalid task data")

    def test_update_task_id_success(self):
        """
        update_task_id => "task updated: <task_id>"
        """
        self.mgr.add_task("Task1", "Desc1")  # id 1
        self.mgr.add_task("Task2", "Desc2")  # id 2
        result = self.mgr.update_task_id(2, "Task2_new", "Desc2_new")
        self.assertEqual(result, "task updated: 2")
        self.assertEqual(self.mgr.tasks[1].title, "Task2_new")
        self.assertEqual(self.mgr.tasks[1].description, "Desc2_new")

    def test_delete_task_id_not_found(self):
        """
        If no task with the given ID => "error: task not found"
        """
        self.mgr.add_task("X", "Y")  # id=1
        result = self.mgr.delete_task_id(999)
        self.assertEqual(result, "error: task not found")

    def test_delete_task_id_success(self):
        """
        If found => "task deleted: <task_id>"
        """
        self.mgr.add_task("T1", "D1")  # id=1
        self.mgr.add_task("T2", "D2")  # id=2
        result = self.mgr.delete_task_id(1)
        self.assertEqual(result, "task deleted: 1")
        self.assertEqual(len(self.mgr.tasks), 1)
        self.assertEqual(self.mgr.tasks[0].task_id, 2)


class TestLevel4(unittest.TestCase):
    """
    Tests for Level 4 – Priority, Completion, Due Dates, Searching
    Adds:
      - set_priority(task_id, priority)
      - complete_task(task_id)
      - list_incomplete_tasks()
      - (Revised) add_task(title, desc, [due_date]) to store due date if valid
      - list_overdue_tasks(reference_date)
      - search_tasks(keyword)
    """

    def setUp(self):
        self.mgr = TaskManager()

    def test_set_priority_errors(self):
        """
        - If no task => "error: task not found"
        - If invalid priority => "error: invalid priority"
        """
        result = self.mgr.set_priority(1, "high")
        self.assertEqual(result, "error: task not found")

        self.mgr.add_task("T1", "D1")  # id=1
        result = self.mgr.set_priority(1, "invalid")
        self.assertEqual(result, "error: invalid priority")

    def test_set_priority_success(self):
        """
        set_priority => "priority set: <task_id>"
        """
        self.mgr.add_task("T1", "D1")  # id=1
        result = self.mgr.set_priority(1, "low")
        self.assertEqual(result, "priority set: 1")
        self.assertEqual(self.mgr.tasks[0].priority, "low")

    def test_complete_task_errors(self):
        """
        If no task => "error: task not found"
        """
        result = self.mgr.complete_task(1)
        self.assertEqual(result, "error: task not found")

    def test_complete_task_success(self):
        """
        complete_task => "task completed: <task_id>"
        sets completed = True
        """
        self.mgr.add_task("T1", "D1")  # id=1
        result = self.mgr.complete_task(1)
        self.assertEqual(result, "task completed: 1")
        self.assertTrue(self.mgr.tasks[0].completed)

    def test_list_incomplete_tasks_none(self):
        """
        If all tasks are complete (or none exist), => "[]"
        """
        self.assertEqual(self.mgr.list_incomplete_tasks(), "[]")

        # Add tasks and complete them
        self.mgr.add_task("T1", "D1")  # id=1
        self.mgr.add_task("T2", "D2")  # id=2
        self.mgr.complete_task(1)
        self.mgr.complete_task(2)
        self.assertEqual(self.mgr.list_incomplete_tasks(), "[]")

    def test_list_incomplete_tasks_some(self):
        """
        Show only incomplete tasks in insertion order => "[Title1, Title2]"
        """
        self.mgr.add_task("Buy milk", "Get 2% milk")   # id=1
        self.mgr.add_task("Call John", "Remind him")   # id=2
        self.mgr.add_task("Meeting notes", "Write up") # id=3

        # Mark only #2 complete
        self.mgr.complete_task(2)
        result = self.mgr.list_incomplete_tasks()
        self.assertEqual(result, "[Buy milk, Meeting notes]")

    def test_add_task_due_date(self):
        """
        We can supply a valid or invalid due_date to add_task.
        Only valid "YYYY-MM-DD" is stored; otherwise it's None.
        The return string is still "task added: <title>, id: <task_id>"
        """
        result1 = self.mgr.add_task("TaskWithDate", "Desc", "2025-12-31")
        self.assertEqual(result1, "task added: TaskWithDate, id: 1")
        self.assertEqual(self.mgr.tasks[0].due_date, "2025-12-31")

        result2 = self.mgr.add_task("TaskInvalidDate", "Desc", "invalid-date")
        # stored as None due to invalid format
        self.assertEqual(result2, "task added: TaskInvalidDate, id: 2")
        self.assertIsNone(self.mgr.tasks[1].due_date)

    def test_list_overdue_tasks_none(self):
        """
        If no tasks are overdue or reference_date is invalid => "[]"
        """
        # add tasks with valid due_dates
        self.mgr.add_task("Task1", "Desc1", "2025-12-31")  # id=1
        self.mgr.add_task("Task2", "Desc2", "2025-01-01")  # id=2
        # reference date invalid => "[]"
        self.assertEqual(self.mgr.list_overdue_tasks("bad-date"), "[]")

        # reference date = "2024-12-31" => no tasks before that
        self.assertEqual(self.mgr.list_overdue_tasks("2024-12-31"), "[]")

    def test_list_overdue_tasks_some(self):
        """
        If a task has due_date < reference_date => it's overdue
        """
        self.mgr.add_task("Task1", "Desc1", "2025-01-01")  # id=1
        self.mgr.add_task("Task2", "Desc2", "2024-12-31")  # id=2
        self.mgr.add_task("Task3", "Desc3")                # id=3, no due_date

        # Reference date "2025-01-01" means tasks strictly before that are overdue
        # Actually "2024-12-31" < "2025-01-01", so that should be overdue
        overdue = self.mgr.list_overdue_tasks("2025-01-01")
        self.assertEqual(overdue, "[Task2]")

    def test_search_tasks_none(self):
        """
        If no tasks match => "[]"
        """
        self.mgr.add_task("Grocery List", "Buy apples and oranges")
        self.mgr.add_task("Work", "Email John about the report")
        result = self.mgr.search_tasks("meeting")
        self.assertEqual(result, "[]")

    def test_search_tasks_some(self):
        """
        search_tasks(keyword) => match in title or description, case-insensitive
        Return titles in insertion order in a Python-style list string
        """
        self.mgr.add_task("Grocery List", "Buy apples and oranges")   # id=1
        self.mgr.add_task("Meeting Prep", "Prepare slides and notes") # id=2
        self.mgr.add_task("Work", "Email John about the meeting")     # id=3

        result1 = self.mgr.search_tasks("apple")
        self.assertEqual(result1, "[Grocery List]")

        result2 = self.mgr.search_tasks("MEETING")
        # matches "Meeting Prep" (title) and "meeting" in "Email John about the meeting"
        self.assertEqual(result2, "[Meeting Prep, Work]")


if __name__ == "__main__":
    unittest.main()
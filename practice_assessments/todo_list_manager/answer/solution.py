class Task:
    """
    A representation of a single to-do item.
    Includes:
      - title (str)
      - description (str)
      - task_id (int)
      - completed (bool)
      - priority (str) in {"low", "medium", "high"}
      - due_date (str or None), expected format "YYYY-MM-DD"
    """
    def __init__(self, task_id, title, description, completed=False,
                 priority="medium", due_date=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        """
        For display in lists, we generally use the title only.
        """
        return self.title


class TaskManager:
    """
    TaskManager handles all the required operations from Levels 1 to 4.
    """

    def __init__(self):
        self.tasks = []            # A list of Task objects
        self.next_id = 1           # Used to assign unique IDs for new tasks

    # ----------------------------------
    # LEVEL 1: add_task + list_tasks
    # ----------------------------------
    def add_task(self, title, description, due_date=None):
        """
        Level 1 (original):
          - If empty title/description => "error: invalid task data"
          - Else => returns "task added: <title>"
        But as of Level 3, we must incorporate IDs:
          - Return => "task added: <title>, id: <task_id>"
        As of Level 4, we also accept optional due_date in "YYYY-MM-DD" format,
        but no changes in the return string.
        Priority is not specified here. We'll set default to "medium".
        """
        if not title or not description:
            return "error: invalid task data"

        # Create the new task with a unique ID
        new_task = Task(
            task_id=self.next_id,
            title=title,
            description=description,
            completed=False,
            priority="medium",
            due_date=self._validate_due_date(due_date)
        )
        self.tasks.append(new_task)
        self.next_id += 1

        # As of Level 3, the correct return is: "task added: <title>, id: <task_id>"
        return f"task added: {title}, id: {new_task.task_id}"

    def list_tasks(self):
        """
        Level 1: list all titles in the order they were added.
        Return format: "[title1, title2]" or "[]"
        """
        if not self.tasks:
            return "[]"
        titles = ", ".join(task.title for task in self.tasks)
        return f"[{titles}]"

    # ----------------------------------
    # LEVEL 2: update_task + delete_task (title-based)
    # ----------------------------------
    def update_task(self, title, new_title, new_description):
        """
        Level 2: update the first task that matches 'title'.
          - If new_title or new_description is empty => "error: invalid task data"
          - If not found => "error: task not found"
          - Else => "task updated: <title>"
        """
        if not new_title or not new_description:
            return "error: invalid task data"

        # Find first match by title
        for task in self.tasks:
            if task.title == title:
                # Found the first matching task
                task.title = new_title
                task.description = new_description
                return f"task updated: {title}"

        return "error: task not found"

    def delete_task(self, title):
        """
        Level 2: delete the first task that matches 'title'.
          - If no such task => "error: task not found"
          - Else => "task deleted: <title>"
        """
        for i, task in enumerate(self.tasks):
            if task.title == title:
                self.tasks.pop(i)
                return f"task deleted: {title}"
        return "error: task not found"

    # ----------------------------------
    # LEVEL 3: IDs introduced + ID-based update/delete
    # ----------------------------------
    def update_task_id(self, task_id, new_title, new_description):
        """
        - If new_title or new_description is empty => "error: invalid task data"
        - If no task with task_id => "error: task not found"
        - Else => "task updated: <task_id>"
        """
        if not new_title or not new_description:
            return "error: invalid task data"

        task = self._find_task_by_id(task_id)
        if task is None:
            return "error: task not found"

        task.title = new_title
        task.description = new_description
        return f"task updated: {task_id}"

    def delete_task_id(self, task_id):
        """
        - If no task with task_id => "error: task not found"
        - Else => "task deleted: <task_id>"
        """
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks.pop(i)
                return f"task deleted: {task_id}"
        return "error: task not found"

    # ----------------------------------
    # LEVEL 4: Priority, Completion, Due Dates, Searching
    # ----------------------------------
    def set_priority(self, task_id, priority):
        """
        - If no task with task_id => "error: task not found"
        - If priority not in {"low","medium","high"} => "error: invalid priority"
        - Else => set the priority, return "priority set: <task_id>"
        """
        task = self._find_task_by_id(task_id)
        if task is None:
            return "error: task not found"

        if priority not in ["low", "medium", "high"]:
            return "error: invalid priority"

        task.priority = priority
        return f"priority set: {task_id}"

    def complete_task(self, task_id):
        """
        - If no task => "error: task not found"
        - Else => set completed=True, return "task completed: <task_id>"
        """
        task = self._find_task_by_id(task_id)
        if task is None:
            return "error: task not found"

        task.completed = True
        return f"task completed: {task_id}"

    def list_incomplete_tasks(self):
        """
        Return titles of all incomplete tasks in order.
        Format: "[title1, title2]" or "[]"
        """
        incompletes = [t.title for t in self.tasks if not t.completed]
        if not incompletes:
            return "[]"
        return f"[{', '.join(incompletes)}]"

    def list_overdue_tasks(self, reference_date):
        """
        - If a task has a valid due_date < reference_date, it's overdue.
        - Return them in insertion order by title: "[title1, title2]" or "[]"
        - If due_date is None or invalid, that task is not considered overdue.
        """
        ref = self._validate_due_date(reference_date)
        if ref is None:
            # If reference_date is invalid format, let's just treat it as no tasks are overdue
            return "[]"

        overdue_titles = []
        for t in self.tasks:
            if t.due_date and t.due_date < ref:
                overdue_titles.append(t.title)

        if not overdue_titles:
            return "[]"
        return f"[{', '.join(overdue_titles)}]"

    def search_tasks(self, keyword):
        """
        - Return titles of tasks whose title or description contains 'keyword' (case-insensitive).
        - If none match, "[]"
        """
        kw_lower = keyword.lower()
        matches = []
        for t in self.tasks:
            if kw_lower in t.title.lower() or kw_lower in t.description.lower():
                matches.append(t.title)

        if not matches:
            return "[]"
        return f"[{', '.join(matches)}]"

    # ----------------------------------
    # Internal Helpers
    # ----------------------------------
    def _find_task_by_id(self, task_id):
        for t in self.tasks:
            if t.task_id == task_id:
                return t
        return None

    def _validate_due_date(self, date_str):
        """
        A simple check that date_str is "YYYY-MM-DD" or None/invalid => return None.
        If valid, return it as a plain string (we rely on lexicographical comparison).
        """
        if not date_str:
            return None
        if len(date_str) == 10 and date_str[4] == "-" and date_str[7] == "-":
            # We won't check if it's a real date, just assume correct format.
            return date_str
        return None
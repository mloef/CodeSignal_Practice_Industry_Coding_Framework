class Task:
    def __init__(self, task_id, title, description, priority="medium"):
        """
        Initialize a new Task.

        Args:
            task_id (int): The unique identifier for the task.
            title (str): The title of the task.
            description (str): The description of the task.
            priority (str, optional): The priority of the task ("low", "medium", or "high").
                                      Defaults to "medium".
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority

    def update(self, new_title, new_description):
        """
        Update the task's title and description.

        Args:
            new_title (str): The new title for the task.
            new_description (str): The new description for the task.
        """
        self.title = new_title
        self.description = new_description

    def __str__(self):
        """
        Return the string representation of the task.
        For listing purposes, only the title is used.
        """
        return self.title


class TaskManager:
    def __init__(self):
        """
        Initialize a new TaskManager.
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, priority="medium"):
        """
        Create a new task with a title, description, and an optional priority.

        Args:
            title (str): The title of the task. Must be non-empty.
            description (str): The description of the task. Must be non-empty.
            priority (str, optional): The priority of the task. Valid values: "low", "medium", "high".
                                      Defaults to "medium".

        Returns:
            str: "task added: <title>" on success, or "error: invalid task data" if title or description is empty.
        """
        if not title or not description:
            return "error: invalid task data"
        if priority not in ["low", "medium", "high"]:
            priority = "medium"
        task = Task(self.next_id, title, description, priority)
        self.tasks.append(task)
        self.next_id += 1
        return f"task added: {title}"

    def list_tasks(self):
        """
        Return a list of all tasks in the order they were added.

        Returns:
            str: A string representation of the list of task titles, formatted as "[task1, task2, ...]".
        """
        task_list = ", ".join(str(task) for task in self.tasks)
        return f"[{task_list}]"

    def update_task(self, task_id, new_title, new_description):
        """
        Update the task identified by task_id with a new title and new description.

        Args:
            task_id (int): The unique identifier of the task.
            new_title (str): The new title for the task.
            new_description (str): The new description for the task.

        Returns:
            str: "task updated: <task_id>" on success,
                 "error: task not found" if the task does not exist,
                 or "error: invalid task data" if new_title or new_description is empty.
        """
        if not new_title or not new_description:
            return "error: invalid task data"
        for task in self.tasks:
            if task.task_id == task_id:
                task.update(new_title, new_description)
                return f"task updated: {task_id}"
        return "error: task not found"

    def delete_task(self, task_id):
        """
        Delete the task identified by task_id.

        Args:
            task_id (int): The unique identifier of the task.

        Returns:
            str: "task deleted: <task_id>" on success,
                 or "error: task not found" if the task does not exist.
        """
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks.pop(i)
                return f"task deleted: {task_id}"
        return "error: task not found"

    def list_tasks_by_priority(self):
        """
        Return a list of tasks sorted by priority in descending order (from high to low).
        If tasks have the same priority, they should be sorted by their creation time (earlier first).

        Returns:
            str: A string representation of the list of task titles, formatted as "[task1, task2, ...]".
        """
        # Define a mapping for priority values for sorting: high -> 3, medium -> 2, low -> 1.
        priority_map = {"high": 3, "medium": 2, "low": 1}
        sorted_tasks = sorted(self.tasks, key=lambda t: (-priority_map[t.priority], t.task_id))
        task_list = ", ".join(str(task) for task in sorted_tasks)
        return f"[{task_list}]"

    def filter_tasks_by_priority(self, priority):
        """
        Return a list of tasks that match the specified priority.

        Args:
            priority (str): The priority to filter tasks by. Must be "low", "medium", or "high".

        Returns:
            str: A string representation of the list of task titles that have the specified priority,
                 formatted as "[task1, task2, ...]". If no tasks match, returns "[]".
        """
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        task_list = ", ".join(str(task) for task in filtered_tasks)
        return f"[{task_list}]"

    def generate_summary_report(self):
        """
        Generate a summary report of the current tasks.

        The report includes:
          - The total number of tasks.
          - A count of tasks for each priority ("high", "medium", "low").

        Returns:
            str: A JSON-formatted string representing the summary report, e.g.,
                 '{"total": 3, "high": 1, "medium": 1, "low": 1}'.
        """
        total = len(self.tasks)
        counts = {"high": 0, "medium": 0, "low": 0}
        for task in self.tasks:
            if task.priority in counts:
                counts[task.priority] += 1
        report = {"total": total, "high": counts["high"], "medium": counts["medium"], "low": counts["low"]}
        import json
        return json.dumps(report)
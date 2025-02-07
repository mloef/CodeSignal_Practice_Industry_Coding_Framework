from collections import OrderedDict
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.tasks = OrderedDict()
        self.id = 0
        self.completed = {}
        self.due_dates = {}
        self.priorities = {}

        self.old_tasks = OrderedDict()


    def add_task(self, title, description):
        if not title or not description:
            return "error: invalid task data"

        if not self.old_tasks.get(title):
            self.old_tasks[title] = []
        
        self.old_tasks[title].append(description)

        return f"task added: {title}"


    def add_task_id(self, title, description, due_date=None):
        if not title or not description:
            return "error: invalid task data"

        self.tasks[self.id] = (title, description)

        if due_date:
            valid_date = False
            try:
                valid_date = datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                pass
            
            if valid_date:
                self.due_dates[self.id] = due_date

        self.id += 1

        return f"task added: {title}, id: {self.id - 1}"


    def list_tasks(self):
        if self.old_tasks:
            return f'[{", ".join(self.old_tasks.keys())}]'
        return f'[{", ".join([x[0] for x in self.tasks.values()])}]'


    def get_task(self, title):
        #return "disabled"
        possible_tasks = self.old_tasks.get(title)

        if not possible_tasks:
            return "error: task not found"

        return f"{title}, {possible_tasks[0]}"


    def update_task(self, title, new_title, new_description):
        #return "disabled"
        if not new_title or not new_description:
            return "error: invalid task data"

        possible_tasks = self.old_tasks.get(title)

        if not possible_tasks:
            return "error: task not found"

        self.old_tasks[title] = possible_tasks[1:]

        if not self.old_tasks.get(new_title):
            self.old_tasks[new_title] = []

        self.old_tasks[new_title].append(new_description)

        return f"task updated: {title}"


    def delete_task(self, title):
        #return "disabled"
        possible_tasks = self.old_tasks.get(title)

        if not possible_tasks:
            return "error: task not found"

        self.old_tasks[title] = possible_tasks[1:]

        return f"task deleted: {title}"


    def delete_task_id(self, id):
        if not self.tasks.get(id):
            return "error: task not found"

        del self.tasks[id]

        return f"task deleted: {id}"


    def get_task_id(self, id):
        task = self.tasks.get(id)

        if not task:
            return "error: task not found"

        priority = self.priorities.get(id)

        if priority:
            return f"{task[0]}, {task[1]}, priority: {priority}"

        return f"{task[0]}, {task[1]}"

    def update_task_id(self, id, new_title, new_description):
        if not new_title or not new_description:
            return "error: invalid task data"

        task = self.tasks.get(id)

        if not task:
            return "error: task not found"

        self.tasks[id] = (new_title, new_description)

        return f"task updated: {id}"
    

    def set_priority(self, id, priority):
        task = self.tasks.get(id)

        if not task:
            return "error: task not found"
        
        if priority not in ["low", "medium", "high"]:
            return "error: invalid priority"

        self.priorities[id] = priority

        return f"priority set: {id}"
    

    def complete_task(self, id):
        task = self.tasks.get(id)

        if not task:
            return "error: task not found"
        
        self.completed[id] = True

        return f"task completed: {id}"
    

    def list_incomplete_tasks(self):
        task_ids = set(self.tasks.keys())

        incomplete_ids = task_ids - set(self.completed.keys())

        return f'[{", ".join([self.tasks[x][0] for x in incomplete_ids])}]'
        

    def list_overdue_tasks(self, reference_date):
        valid_date = False
        try:
            valid_date = datetime.strptime(reference_date, '%Y-%m-%d')
        except ValueError:
            pass

        if not valid_date:
            return "[]"
        

        result = []

        for id, due_date in self.due_dates.items():
            if due_date < reference_date:
                result.append(self.tasks[id][0])
        
        return f'[{", ".join(result)}]'


    def search_tasks(self, keyword):
        matches = []

        keyword = keyword.lower()

        for title, description in self.tasks.values():
            if keyword in title.lower() or keyword in description.lower():
                matches.append(title)

        return f'[{", ".join(matches)}]'
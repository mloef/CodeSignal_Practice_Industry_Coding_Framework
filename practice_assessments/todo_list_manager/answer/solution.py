from collections import OrderedDict
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"

class Task:
   def __init__(self, title, description, due_date = None):
      self.title = title
      self.description = description
      self.due_date = due_date
      self.priority = None
      self.completed = False


class TaskManager:
   def __init__(self):
      self.tasks = OrderedDict()
      self.last_id = -1

   def add_task(self, title, description, due_date=None):
      if not title or not description:
         raise ValueError("Invalid task data: parameters must not be empty")
      
      if due_date:
         try:
            due_date = datetime.strptime(due_date, DATE_FORMAT)
         except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

      self.last_id += 1  
      self.tasks[self.last_id] = Task(title, description, due_date)

      return f"task added: {title}"

   def add_task_by_id(self, title, description, due_date=None):
      return self.add_task(title, description, due_date) + ", id: " + str(self.last_id)
         
   def list_tasks(self, priority = None):
      if priority:
         self._validate_priority(priority)
         titles = [task.title for task in self.tasks.values() if task.priority is priority]
      else:
         titles = [task.title for task in self.tasks.values()]

      return f"[{', '.join(titles)}]"

   def _title_to_id(self, title):
      if not title:
         raise ValueError("Invalid task data: parameters must not be empty")
      
      task_id = None

      for id, task in self.tasks.items():
         if task.title == title:
            task_id = id
            break
      
      # not strictly necessary because we always catch
      # it in _get_task_by_id below
      if task_id is None:
         raise KeyError("Task not found")

      return task_id

   def _get_task_by_id(self, task_id):
      task = self.tasks.get(task_id)

      if task is None:
         raise KeyError("Task not found")
      
      return task

   def get_task(self, title):
      task_id = self._title_to_id(title)
      
      return self.get_task_by_id(task_id)
   
   def get_task_by_id(self, task_id):
      task = self._get_task_by_id(task_id)

      suffix = ""
      if task.completed:
         suffix += ", completed: True"
      if task.priority:
         suffix += f", priority: {task.priority}"
      if task.due_date:
         suffix += f", due date: {task.due_date.strftime(DATE_FORMAT)}"
      
      return f"{task.title}, {task.description}" + suffix
      
   def _update_task_by_id(self, task_id, new_title, new_description):
      if not new_title or not new_description:
         raise ValueError("Invalid task data: parameters must not be empty")
      
      self._get_task_by_id(task_id) # throws if task does not exist
      
      del self.tasks[task_id] # for ordering
      self.tasks[task_id] = Task(new_title, new_description)

      return "task updated: "

   def update_task(self, title, new_title, new_description):
      task_id = self._title_to_id(title)
      
      return self._update_task_by_id(task_id, new_title, new_description) + title

   def update_task_by_id(self, task_id, new_title, new_description):
      return self._update_task_by_id(task_id, new_title, new_description) + str(task_id)
   
   def _delete_task_by_id(self, task_id):
      self._get_task_by_id(task_id) # throws if task does not exist
      
      del self.tasks[task_id]
      return "task deleted: "

   def delete_task(self, title):
      task_id = self._title_to_id(title)

      return self._delete_task_by_id(task_id) + title
   
   def delete_task_by_id(self, task_id):
      return self._delete_task_by_id(task_id) + str(task_id)
   
   def complete_task(self, task_id):
     self._get_task_by_id(task_id).completed = True
     return f"task completed: {task_id}"
   
   def list_incomplete_tasks(self):
      titles = [task.title for task in self.tasks.values() if not task.completed]
      return f"[{', '.join(titles)}]"
   
   def list_overdue_tasks(self, reference_date):
      try:
         reference_date = datetime.strptime(reference_date, DATE_FORMAT)
      except ValueError:
         raise ValueError("Invalid date format. Use YYYY-MM-DD")
      
      titles = [task.title for task in self.tasks.values() if task.due_date and task.due_date < reference_date]
      return f"[{', '.join(titles)}]"
    
   def search_tasks(self, keyword):
      keyword = keyword.lower()
      titles = [task.title for task in self.tasks.values() if keyword in task.title.lower() or keyword in task.description.lower()]
      return f"[{', '.join(titles)}]"
   
   def _validate_priority(self, priority):
      if priority not in ["low", "medium", "high"]:
         raise ValueError("Invalid priority value")

   def set_priority(self, task_id, priority):
      self._validate_priority(priority)
      self._get_task_by_id(task_id).priority = priority

      return f"priority set: {task_id}"


# TODO: think about how to make this neater and clearer to read, with less code golf
# Level 1 – Add, List and Get

In this initial level, you must implement three functions:

1. `add_task(title, description)`
2. `list_tasks()`
3. `get_task(title)`

---

## 1. `add_task(title, description)`

**Purpose**
Create a new task using the two string parameters `title` and `description`.

**Expected Behavior**
1. If either `title` or `description` is an empty string, return:
   ```
   error: invalid task data
   ```
2. Otherwise, return:
   ```
   task added: <title>
   ```
   where `<title>` is replaced by the task's title.

**Example Usage**
```
add_task("Buy milk", "Get 2% milk")
→ "task added: Buy milk"
```

---

## 2. `list_tasks()`

**Purpose**
Return all task titles in the order they were added, oldest first.

**Expected Behavior**
- If tasks exist, return them in a Python-style list of titles, for example:
  ```
  [Buy milk, Call John]
  ```
- If no tasks exist, return:
  ```
  []
  ```

**Example Usage**
```
add_task("Buy milk", "Get 2% milk")
add_task("Call John", "Call John at 10:00")
list_tasks()
→ "[Buy milk, Call John]"
```

---

## 3. `get_task(title)`

**Purpose**
Return the task's title and description for the task matching the given `title`.

**Expected Behavior**
1. If a task with the matching `title` exists (if multiple exist, choose the first one added), return:
   ```
   <title>, <description>
   ```
2. If no such task exists, return:
   ```
   error: task not found
   ```

**Example Usage**
```
add_task("Buy milk", "Get 2% milk")
get_task("Buy milk")
→ "Buy milk, Get 2% milk"
```

---

## Boilerplate

You may copy the below framework code into your solution file.

```python
class TaskManager:
   def __init__(self):
        pass
   
   def add_task(self, title, description):
       pass
   
   def list_tasks(self):
       pass
   
   def get_task(self, title):
       pass
```

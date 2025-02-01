# Level 1 – Basic Add and List

In this initial level, you must implement two functions:

1. `add_task(title, description)`
2. `list_tasks()`

No unique ID is involved yet.

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
   where `<title>` is replaced by the task’s title.

**Example Usage**
```
add_task("Buy milk", "Get 2% milk")
→ "task added: Buy milk"
```

---

## 2. `list_tasks()`

**Purpose**
Return all task titles in the order they were added.

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
list_tasks()
→ "[Buy milk, Call John]"
```

---

## Important Notes

- **No unique identifiers** (IDs) are introduced at this level.
- A naive design might simply store `(title, description)` pairs in a list, which is sufficient for Level 1.
- Your return strings must match exactly. Even small formatting differences can cause test failures.
# Task Tracker CLI

A simple command-line task tracker built in Python, using only the standard library. This is a practice project based on the [roadmap.sh Task Tracker challenge](https://roadmap.sh/projects/task-tracker), used to build core Python fundamentals: argument parsing, file I/O, JSON handling, and error handling — without relying on external libraries or frameworks.

## Features

- Add, update, and delete tasks
- Mark tasks as `in-progress` or `done`
- List all tasks, or filter by status (`todo`, `in-progress`, `done`)
- Tasks persist between runs, stored locally in a JSON file
- Handles common edge cases: missing arguments, invalid IDs, corrupted or missing data file

## Requirements

- Python 3.x
- No external libraries or packages required — everything used is part of the Python standard library (`sys`, `json`, `os`, `datetime`)

## Getting Started

Clone the repository and run the script directly with Python:

```bash
git clone <your-repo-url>
cd Task-Tracker
python3 task_tracker.py <command> [arguments]
```

A `task_list.json` file will be created automatically in the same folder the first time you add a task.

## Usage

### Add a task

```bash
python3 task_tracker.py add "Buy groceries"
```
```
['Buy groceries'] is added
```

### Update a task's description

```bash
python3 task_tracker.py update 1 "Buy groceries and cook dinner"
```
```
Task 1 has been updated with Buy groceries and cook dinner
```

### Delete a task

```bash
python3 task_tracker.py delete 1
```
```
Task 1 has been deleted
```

### Mark a task as in-progress

```bash
python3 task_tracker.py mark-in-progress 1
```
```
Task 1 has been updated
```

### Mark a task as done

```bash
python3 task_tracker.py mark-done 1
```
```
Task 1 has been updated
```

### List all tasks

```bash
python3 task_tracker.py list
```

### List tasks by status

```bash
python3 task_tracker.py list todo
python3 task_tracker.py list in-progress
python3 task_tracker.py list done
```

## Task Properties

Each task is stored as a JSON object with the following fields:

| Field         | Type   | Description                                  |
|---------------|--------|-----------------------------------------------|
| `id`          | int    | Unique identifier, auto-incremented           |
| `description` | string | The task text                                 |
| `status`      | string | One of `todo`, `in-progress`, `done`          |
| `CreatedAt`   | string | Timestamp when the task was created            |
| `UpdatedAt`   | string | Timestamp of the most recent update            |

Tasks are stored as a list of these objects in `task_list.json`:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "CreatedAt": "09/07/2026 19:55:40",
        "UpdatedAt": "09/07/2026 19:55:40"
    }
]
```

## Error Handling

The CLI validates input and fails with a clear message instead of crashing, for cases including:

- No command provided
- Unrecognized command
- Wrong number of arguments for a command (e.g. `add` with no description)
- Non-numeric task ID (e.g. `delete abc`)
- Task ID that doesn't exist (e.g. `update 999 "..."`)
- Invalid status filter passed to `list` (e.g. `list foo`)
- Missing or corrupted `task_list.json` — the program falls back to an empty task list rather than crashing

## What I Learned

- How Python parses command-line arguments through `sys.argv`, and how to build validation with guard clauses before accessing potentially missing values
- The difference between lists and dictionaries, and when a list of dictionaries is the right data model for structured records
- Reading and writing JSON with the `json` module, and handling the case where the data file doesn't exist yet or contains invalid JSON
- How `try`/`except` is used for validating input (converting strings to integers) as well as for handling file/data errors — and how keeping `try` blocks narrow avoids accidentally catching unrelated errors
- That variables referencing dictionaries inside a list point to the same object, so mutating a dictionary found via a loop updates it directly in the original list
- Recognizing repeated logic across multiple commands (finding a task by ID) and extracting it into a shared function (`find_task`) instead of duplicating it

## Project Status

Core functionality is complete: add, update, delete, mark-in-progress, mark-done, and list (with and without status filtering) all work and persist data correctly across runs.

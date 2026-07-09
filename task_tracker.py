import sys
import json
import os
import datetime

if len(sys.argv) < 2:
    sys.exit("Enter a value to make changes in tasks")

COMMAND = sys.argv[1]
REST = sys.argv[2: ]

def load_tasks():
    if os.path.exists("task_list.json"):
        with open("task_list.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        with open("task_list.json", mode="w") as write_file:
            json.dump([], write_file)
        return []


def save_tasks(tasks):
    with open("task_list.json", "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

def get_next_id(tasks):
    for task in tasks:
        if task["id"] == task_id:
            return task_id + 1
    return None

    temp_list = []
    for task in tasks:
        temp_list.append(task["id"])
    
    try:
        return max(temp_list) + 1
    except ValueError:
        return 1

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

if COMMAND == "add":
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if len(REST) != 1:
        sys.exit("Enter task values (minimum 1)")
    else:
        new_dict = {"id": get_next_id(tasks), "description": REST[0], "status": "todo", "CreatedAt": current_time, "UpdatedAt": current_time}
        tasks.append(new_dict)
        save_tasks(tasks)

        print(f"{REST} is added")

elif COMMAND == "update":
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if len(REST) != 2:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(REST[0])
        except ValueError:
            sys.exit("Task ID must be a number")
    
    task = find_task(tasks, task_id)

    if not task:
        print(f"No task with {task_id} found.")
    else:
        task["UpdatedAt"] = current_time
        task["description"] = REST[1]
        save_tasks(tasks)
        print(f"Task {task_id} has been updated with {REST[1]}")

elif COMMAND == "delete":
    if len(REST) != 1:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(REST[0])
        except ValueError:
            sys.exit("Task ID mist be a number")
    
    task = find_task(tasks, task_id)

    if not task:
        print(f"No task with {task_id} found.")
    else:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task {task_id} has been deleted")


elif COMMAND == "mark-in-progress":
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if len(REST) != 1:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(REST[0])
        except ValueError:
            sys.exit("Task ID must be a number")
    
    task = find_task(tasks, task_id)

    if not task:
        print(f"No task with {task_id} found.")
    else:
        task["UpdatedAt"] = current_time
        task["status"] = "in-progress"
        save_tasks(tasks)
        print(f"Task {task_id} has been updated")

elif COMMAND == "mark-done":
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if len(REST) != 1:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(REST[0])
        except ValueError:
            sys.exit("Task ID must be a number")
    task = find_task(tasks, task_id)

    if not task:
        print(f"No task with {task_id} found.")
    else:
        task["UpdatedAt"] = current_time
        task["status"] = "done"
        save_tasks(tasks)
        print(f"Task {task_id} has been updated")

elif COMMAND == "list":
    valid_statuses = ["todo", "in-progress", "done"]
    temp_matching_tasks = []
    if len(REST) > 1:
        sys.exit("Enter task values")
    else:
        if REST:
            if REST[0] not in valid_statuses:
                print("Please enter either todo, done, or in-progress after list")
            else:
                for task in tasks:
                    if task["status"] == REST[0]:
                        temp_matching_tasks.append(task)
                if temp_matching_tasks:
                    print(temp_matching_tasks)
                else:
                    print("No task found")
        else:
            for task in tasks:
                print(task)

else:
    sys.exit(f"Unkown COMMAND: {COMMAND}")



import sys

if len(sys.argv) < 2:
    sys.exit("Enter a value to make changes in tasks")

command = sys.argv[1]
rest = sys.argv[2: ]


if command == "add":
    if len(rest) != 1:
        sys.exit("Enter task values (minimum 1)")
    else:
        print(f"{rest} is added")

elif command == "update":
    if len(rest) != 2:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(rest[0])
        except ValueError:
            sys.exit("Task ID must be a number")
        print(f"updated {rest}")

elif command == "delete":
    if len(rest) != 1:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(rest[0])
        except ValueError:
            sys.exit("Task ID must be a number")
        print(f"placeholder: {rest}")

elif command == "mark-in-progress":
    if len(rest) != 1:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(rest[0])
        except ValueError:
            sys.exit("Task ID must be a number")
        print(f"The following are the tasks: {rest}")

elif command == "mark-done":
    if len(rest) != 1:
        sys.exit("Enter task values")
    else:
        try:
            task_id = int(rest[0])
        except ValueError:
            sys.exit("Task ID must be a number")
        print(f"The following are the tasks: {rest}")

elif command == "list":
    if len(rest) > 1:
        print(len(rest))
        sys.exit("Enter task values")
    else:
        print(f"The following are the tasks: {rest}")
        print(len(rest))

else:
    sys.exit(f"Unkown command: {command}")
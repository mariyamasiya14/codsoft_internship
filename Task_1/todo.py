import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n--------- YOUR TASKS ---------")

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task['task']} - {status}")

def complete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def update_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to update: "))

        if 1 <= task_number <= len(tasks):

            new_task = input("Enter the new task: ")

            if new_task.strip() == "":
                print("Task cannot be empty!")
                return

            tasks[task_number - 1]["task"] = new_task

            save_tasks(tasks)
            print("Task updated successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            deleted_task = tasks.pop(task_number - 1)

            save_tasks(tasks)

            print("Deleted:", deleted_task["task"])

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

tasks = load_tasks()

while True:

    print("\n================================")
    print("          MY TO-DO LIST")
    print("================================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        update_task(tasks)

    elif choice == "5":
        delete_task(tasks)

    elif choice == "6":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
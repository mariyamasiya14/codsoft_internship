import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# -----------------------------

# -----------------------------

FILE_NAME = "tasks.json"


# -----------------------------
# Load tasks from file
# -----------------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# -----------------------------
# Save tasks to file
# -----------------------------

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Update task count
# -----------------------------

def update_count():
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    count_label.config(
        text=f"Total: {total}    Pending: {pending}    Completed: {completed}"
    )


# -----------------------------
# Display tasks
# -----------------------------

def display_tasks():
    for item in task_tree.get_children():
        task_tree.delete(item)

    for index, task in enumerate(tasks):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        task_tree.insert(
            "",
            "end",
            iid=index,
            values=(index + 1, task["task"], status)
        )

    update_count()


# -----------------------------
# Add task
# -----------------------------

def add_task():

    task_name = task_entry.get().strip()

    if task_name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )
        return

    tasks.append({
        "task": task_name,
        "completed": False
    })

    save_tasks()
    display_tasks()

    task_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Task added successfully!"
    )


# -----------------------------
# Get selected task
# -----------------------------

def get_selected_task():

    selected = task_tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task first."
        )
        return None

    return int(selected[0])


# -----------------------------
# Mark task as completed
# -----------------------------

def complete_task():

    index = get_selected_task()

    if index is None:
        return

    tasks[index]["completed"] = True

    save_tasks()
    display_tasks()

    messagebox.showinfo(
        "Success",
        "Task marked as completed!"
    )


# -----------------------------
# Update task
# -----------------------------

def update_task():

    index = get_selected_task()

    if index is None:
        return

    new_task = task_entry.get().strip()

    if new_task == "":
        messagebox.showwarning(
            "Warning",
            "Enter the new task in the input box."
        )
        return

    tasks[index]["task"] = new_task

    save_tasks()
    display_tasks()

    task_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Task updated successfully!"
    )


# -----------------------------
# Delete task
# -----------------------------

def delete_task():

    index = get_selected_task()

    if index is None:
        return

    result = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this task?"
    )

    if result:

        tasks.pop(index)

        save_tasks()
        display_tasks()

        messagebox.showinfo(
            "Success",
            "Task deleted successfully!"
        )


# -----------------------------
# Select task and show in input
# -----------------------------

def select_task(event):

    selected = task_tree.selection()

    if selected:

        index = int(selected[0])

        task_entry.delete(0, tk.END)

        task_entry.insert(
            0,
            tasks[index]["task"]
        )


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()

window.title("To-Do List Application")

window.geometry("700x550")

window.resizable(False, False)


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    window,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


# -----------------------------
# Input frame
# -----------------------------

input_frame = tk.Frame(window)

input_frame.pack(pady=10)


task_entry = tk.Entry(
    input_frame,
    width=45,
    font=("Arial", 12)
)

task_entry.grid(
    row=0,
    column=0,
    padx=10
)


add_button = tk.Button(
    input_frame,
    text="Add Task",
    width=12,
    command=add_task
)

add_button.grid(
    row=0,
    column=1
)


# -----------------------------
# -----------------------------

columns = ("No", "Task", "Status")


task_tree = ttk.Treeview(
    window,
    columns=columns,
    show="headings",
    height=12
)


task_tree.heading(
    "No",
    text="No."
)

task_tree.heading(
    "Task",
    text="Task"
)

task_tree.heading(
    "Status",
    text="Status"
)


task_tree.column(
    "No",
    width=60,
    anchor="center"
)

task_tree.column(
    "Task",
    width=400
)

task_tree.column(
    "Status",
    width=150,
    anchor="center"
)


task_tree.pack(
    pady=20
)


# Select event

task_tree.bind(
    "<<TreeviewSelect>>",
    select_task
)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(window)

button_frame.pack(pady=10)


complete_button = tk.Button(
    button_frame,
    text="Mark Completed",
    width=15,
    command=complete_task
)

complete_button.grid(
    row=0,
    column=0,
    padx=5
)


update_button = tk.Button(
    button_frame,
    text="Update Task",
    width=15,
    command=update_task
)

update_button.grid(
    row=0,
    column=1,
    padx=5
)


delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=15,
    command=delete_task
)

delete_button.grid(
    row=0,
    column=2,
    padx=5
)


# -----------------------------
# Task count
# -----------------------------

count_label = tk.Label(
    window,
    text="Total: 0    Pending: 0    Completed: 0",
    font=("Arial", 11)
)

count_label.pack(pady=15)


# -----------------------------
# Load existing tasks
# -----------------------------

tasks = load_tasks()

display_tasks()


# -----------------------------
# Start application
# -----------------------------

window.mainloop()
import sys
import os

# Define the filename where tasks will be stored
TASKS_FILE = "tasks.txt"

# Load tasks from the file, returning a list of tasks
def load_tasks():
    tasks = []
    # Check if tasks file exists
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    tasks.append(line)
    return tasks

# Save the current list of tasks back to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task with the provided description
def add_task(description):
    tasks = load_tasks()  # Load current tasks
    tasks.append(description)  # Add new task to list
    save_tasks(tasks)  # Save updated list
    print(f'Task added: "{description}"')

# List all pending tasks
def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("Pending Tasks:")
        # Print each task with a number
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No pending tasks.")

# Mark a specific task as completed and remove it from the list
def complete_task(task_number):
    tasks = load_tasks()
    # Check if the task number is valid
    if 0 < task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)  # Remove the task
        save_tasks(tasks)  # Save updated list
        print(f'Task completed: "{completed_task}"')
    else:
        print("Invalid task number.")

# Delete a specific task from the list
def delete_task(task_number):
    tasks = load_tasks()
    # Check if the task number is valid
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)  # Remove the task
        save_tasks(tasks)  # Save updated list
        print(f'Task deleted: "{deleted_task}"')
    else:
        print("Invalid task number.")

# Main function to handle command-line arguments and call appropriate functions
def main():
    # Check if at least one argument (the command) is provided
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py [add|list|complete|delete] <arguments>")
        return

    # Get the command (e.g., "add", "list", "complete", or "delete")
    command = sys.argv[1]

    if command == "add":
        # Check if task description is provided
        if len(sys.argv) < 3:
            print("Please provide a task description.")
        else:
            # Join all words in the description as a single string
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        list_tasks()

    elif command == "complete":
        # Check if task number is provided
        if len(sys.argv) < 3:
            print("Please provide the task number to complete.")
        else:
            try:
                task_number = int(sys.argv[2])
                complete_task(task_number)
            except ValueError:
                print("Invalid task number.")

    elif command == "delete":
        # Check if task number is provided
        if len(sys.argv) < 3:
            print("Please provide the task number to delete.")
        else:
            try:
                task_number = int(sys.argv[2])
                delete_task(task_number)
            except ValueError:
                print("Invalid task number.")

    else:
        print("Unknown command. Use 'add', 'list', 'complete', or 'delete'.")

# Entry point of the script
if __name__ == "__main__":
    main()

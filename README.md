# Writing the README content to a .md file for the user.

# Define the README content
readme_content = """
# Task Manager CLI Tool

This is a simple command-line interface (CLI) tool for managing tasks. You can add, view, complete, and delete tasks, with all tasks saved to a text file (`tasks.txt`) to ensure persistence across sessions.

## Features

- **Add a Task**: Add a new task with a description.
- **View Tasks**: List all pending tasks.
- **Complete a Task**: Mark a task as completed.
- **Delete a Task**: Remove a task from the list.

## Requirements

- Python 3.x

## Setup

1. Clone or download this repository.
2. Navigate to the directory containing `task_manager.py`.
3. Ensure Python 3 is installed and accessible from your command line.

## Usage

Run the tool by using the following command structure:
```bash
python task_manager.py [command] <arguments>

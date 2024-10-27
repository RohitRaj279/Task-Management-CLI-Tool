
# Task Manager CLI Tool

This is a simple command-line interface (CLI) tool for managing tasks. You can add, view, complete, and delete tasks, with all tasks saved to a text file (`tasks.txt`) to ensure persistence across sessions.

## Features

- **Add a Task**: Add a new task with a description.
- **View Tasks**: List all pending tasks.
- **Complete a Task**: Mark a task as completed.
- **Delete a Task**: Remove a task from the list.
- **Persistence**: Tasks are stored in a text file, so they are saved between program runs.

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
```

### Commands

1. **Add a Task**
   - Adds a task with a specified description.
   - **Usage**:
     ```bash
     python task_manager.py add "<task_description>"
     ```
   - **Example**:
     ```bash
     python task_manager.py add "Buy groceries"
     ```
   - **Output**:
     ```
     Task added: "Buy groceries"
     ```

2. **View Tasks**
   - Lists all pending tasks with a numbered list.
   - **Usage**:
     ```bash
     python task_manager.py list
     ```
   - **Output** (Example):
     ```
     Pending Tasks:
     1. Buy groceries
     2. Clean the house
     ```

3. **Complete a Task**
   - Marks a specified task as completed and removes it from the list.
   - **Usage**:
     ```bash
     python task_manager.py complete <task_number>
     ```
   - **Example**:
     ```bash
     python task_manager.py complete 1
     ```
   - **Output**:
     ```
     Task completed: "Buy groceries"
     ```

4. **Delete a Task**
   - Deletes a specified task from the list.
   - **Usage**:
     ```bash
     python task_manager.py delete <task_number>
     ```
   - **Example**:
     ```bash
     python task_manager.py delete 1
     ```
   - **Output**:
     ```
     Task deleted: "Clean the house"
     ```

## Notes

- The tasks are stored in `tasks.txt` within the same directory as `task_manager.py`, allowing data to persist between sessions.
- Task numbers are automatically adjusted as tasks are added, completed, or deleted.

## Example Usage

```bash
# Add tasks
python task_manager.py add "Buy groceries"
python task_manager.py add "Clean the house"
python task_manager.py add "Finish the report"

# List tasks
python task_manager.py list

# Complete a task
python task_manager.py complete 1

# List tasks again to see updates
python task_manager.py list

# Delete a task
python task_manager.py delete 2

# Final list of tasks
python task_manager.py list
```

## Test Cases

The following test cases demonstrate each command along with expected output:

1. **Add Task**:
   ```bash
   python task_manager.py add "Buy groceries"
   ```
   **Expected Output**:
   ```
   Task added: "Buy groceries"
   ```

2. **Add Another Task**:
   ```bash
   python task_manager.py add "Clean the house"
   ```
   **Expected Output**:
   ```
   Task added: "Clean the house"
   ```

3. **Add a Third Task**:
   ```bash
   python task_manager.py add "Finish the report"
   ```
   **Expected Output**:
   ```
   Task added: "Finish the report"
   ```

4. **View Tasks**:
   ```bash
   python task_manager.py list
   ```
   **Expected Output**:
   ```
   Pending Tasks:
   1. Buy groceries
   2. Clean the house
   3. Finish the report
   ```

5. **Complete Task (Mark the First Task as Completed)**:
   ```bash
   python task_manager.py complete 1
   ```
   **Expected Output**:
   ```
   Task completed: "Buy groceries"
   ```

6. **View Tasks After Completion**:
   ```bash
   python task_manager.py list
   ```
   **Expected Output**:
   ```
   Pending Tasks:
   1. Clean the house
   2. Finish the report
   ```

7. **Delete Task (Delete the First Task in the Current List)**:
   ```bash
   python task_manager.py delete 1
   ```
   **Expected Output**:
   ```
   Task deleted: "Clean the house"
   ```

8. **View Tasks After Deletion**:
   ```bash
   python task_manager.py list
   ```
   **Expected Output**:
   ```
   Pending Tasks:
   1. Finish the report
   ```

9. **Complete All Remaining Tasks (Clean Up for Next Tests)**:
   ```bash
   python task_manager.py complete 1
   ```
   **Expected Output**:
   ```
   Task completed: "Finish the report"
   ```

10. **View Tasks After All Tasks Are Completed**:
    ```bash
    python task_manager.py list
    ```
    **Expected Output**:
    ```
    No pending tasks.
    ```

## License

This project is free to use and distribute.

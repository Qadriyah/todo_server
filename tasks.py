todo_list = []


def create_task(task):
    """
    Adds a task to the todo list.

    Args: 
        task(str): The task to be created

    Returns: 
        tuple: With two elements, amessage and a bool. 
        ('success', True), ('Failure', False)
    """

    #  Check if task already exists
    if task in todo_list:
        return "Task already exists", False

    #  Create a new task
    todo_list.append(task)
    return "Task has been created successfully", True


def delete_task(task):
    """
    Removes the specified task from the todo list.

    Args:
        task(str): The task to be removed

    Returns: 
        tuple: With two elements, a message and a bool. 
        ('success', True), ('Failure', False)
    """

    #  Check if the todo list is empty
    if len(todo_list) == 0:
        return "There are no items in your todo list", False

    #  Check if the selected task exists
    if task not in todo_list:
        return "Selected task does not exist", False

    #  Remove the selected task
    todo_list.remove(task)
    return "Selected task has been deleted successfully", True


def mark_as_finished(task):
    """
    Appends a label '[finished]' at the end of the task to 
    indicate that the task has been finished.

    Args:
        task(str): The task to be labelled

    Returns: 
        tuple: With two elements, a message and a bool. 
        ('success', True), ('Failure', False)
    """

    #  Check if the selected task is already marked as finished
    if "finished" in task:
        return "The selected task has already been finished", False

    task_position = todo_list.index(task)
    todo_list[task_position] = task + " [finished]"
    return "Task has been marked successfully", True


def delete_all_tasks():
    """
    Deletes all tasks from the todo list
    """

    todo_list.clear()


def display_todo_list():
    """
    Prints all tasks in the todo list
    """

    print("\n----------------------------------------")
    print("Your Tasks")
    print("----------------------------------------")
    for i, item in enumerate(todo_list):
        print("{}. {}".format(i+1, item))
    print("----------------------------------------")


def is_list_empty():
    """
    Checks if the todo list is empty

    Returns:
        bool: True for success, False otherwise
    """
    if len(todo_list) == 0:
        return True
    return False


def is_task_in_the_list(task_position):
    """
    Checks if the selected task in the todo list

    Args:
        task_position(int): The position of the task in the todo list

    Returns:
        bool: True for success, False otherwise
    """

    items = [i for i, item in enumerate(todo_list)]
    if task_position not in items:
        return False
    return True

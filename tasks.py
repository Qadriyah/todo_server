todo_list = []


def create_task(task):
    """
    Adds a task to the todo list. Returns tuple with two values, 
    a boolean and a message

    Argument: 
    task -- The task to be created
    """

    #  Check if task already exists
    if task in todo_list:
        return "Task already exists", False

    #  Create a new task
    todo_list.append(task)
    return "Task has been created successfully", True


def delete_task(task):
    """
    Removes the specified task from the todo list. Returns 
    a tuple with two values, a boolean and a message

    Arguments:
    task -- The task to be removed
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
    indicate that the task has been finished. Returns a tuple 
    with two values, a boolean and message.

    Arguments:
    task    -- the task to be labelled
    """

    #  Check if the selected task is already marked as finished
    if "finished" in task:
        return "The selected task has already been finished", False

    task_position = todo_list.index(task)
    todo_list[task_position] = task + " [finished]"
    return "Task has been marked successfully", True


def delete_all_tasks():
    """
    Empty the todo list
    """

    todo_list.clear()

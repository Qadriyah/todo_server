todo_list = []


def create_task(task):
    """
    Add the task to the todo list
    """

    todo_list.append(task)


def delete_task(task):
    """
    Removes the specified task from the todo list
    """

    todo_list.remove(task)

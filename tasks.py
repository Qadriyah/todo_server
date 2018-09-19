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


def mark_as_finished(task):
    """
    Appends a label '[finished]' at the end of the task
    """

    task_position = task_list.index(task)
    todo_list[task_position] = task + " [finished]"


def delete_all_tasks():
    """
    Empty the todo list
    """

    todo_list.clear()

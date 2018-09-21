import time

from accounts import *
from tasks import *

menu = {
    1: "Create task",
    2: "Delete task",
    3: "Delete all tasks",
    4: "Mark task as finished",
    5: "Display all tasks",
    6: "Logout"
}


def main():
    print("\nMenu")
    for key, value in menu.items():
        print("{}. {}".format(key, value))

    selected_option = input("\nSelect an option: ")
    try:
        selected_option = int(selected_option)

        #  Check if the selected option exists on the task list
        menu_options = list(menu.keys())
        if selected_option not in menu_options:
            print("[+] The selected item does not exists\n")
            main()

        if selected_option == 1:
            task = input("\nEnter your task: ")
            print("[+] Creating your task...")
            time.sleep(2)
            result = create_task(task)
            print("[+] {}\n".format(result[0]))
            main()

        if selected_option == 2:
            #  Check if the todo list is empty
            if len(todo_list) == 0:
                print("[+] There are no items in your todo list")
                main()

            #  Print a list of todos
            print("\nYour Tasks")
            for i, item in enumerate(todo_list):
                print("{}. {}".format(i+1, item))

            selected_task = input("\nSelect a task to delete: ")
            print("[+] Deleting task...")
            time.sleep(2)

            #  Check if the seleted item is on the list
            items = [i for i, item in enumerate(todo_list)]
            if int(selected_task) - 1 not in items:
                print("[+] The selected task is not on the list\n")
                main()

            #  Delete the selected task from the list
            result = delete_task(todo_list[int(selected_task) - 1])
            print("[+] {}\n".format(result[0]))
            main()

        if selected_option == 3:
            #  Check if the todo list is empty
            if len(todo_list) == 0:
                print("[+] There are no items in your todo list")
                main()

            print("\n[+] Deleting all tasks...")
            time.sleep(2)
            delete_all_tasks()
            print("[+] Tasks have been deleted successfully\n")
            main()

        if selected_option == 4:
            #  Check if the todo list is empty
            if len(todo_list) == 0:
                print("[+] There are no items in your todo list")
                main()

            print("\nYour Tasks")
            for i, item in enumerate(todo_list):
                print("{}. {}".format(i+1, item))

            selected_task = input("\nSelect a finished task: ")
            print("[+] Marking task as finished...")
            time.sleep(2)

            #  Check if the seleted task is on the list
            items = [i for i, item in enumerate(todo_list)]
            if int(selected_task) - 1 not in items:
                print("[+] The selected task is not on the list\n")
                main()

            #  Mark task as finished
            result = mark_as_finished(todo_list[int(selected_task) - 1])
            print("[+] {}\n".format(result[0]))
            main()

        if selected_option == 5:
            #  Check if the todo list is empty
            if len(todo_list) == 0:
                print("[+] There are no items in your todo list")
                main()

            for i, item in enumerate(todo_list):
                print("{}. {}".format(i+1, item))
            main()

        if selected_option == 6:
            print("\n[+] Logging out...")
            time.sleep(2)
            print("[+] You have been logged out\n")

    except ValueError:
        print("[+] Your option should be a number\n")
        main()


def unregistered(name, password):
    #  Create an account for the user
    print("[+] Registering user...")
    time.sleep(2)
    add_account(name, password)
    print("[+] User registered successfully\n")


if __name__ == "__main__":
    """
    Get user inputs
    """
    print("\n::::::::::::: My Todo App ::::::::::::::::::\n")
    name = input("Enter your name: ")
    password = input("Enter password: ")

    if login(name, password):
        print("[+] Logging in...")
        main()
    else:
        unregistered(name, password)
        main()

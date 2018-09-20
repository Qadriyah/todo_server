import time

from accounts import accounts, add_account, login
from tasks import todo_list, create_task, delete_task, mark_as_finished, delete_all_tasks

menu = {
    1: "Create task",
    2: "Delete task",
    3: "Delete all tasks",
    4: "Mark task as finished",
    5: "Display all tasks",
    6: "Logout"
}


def main():
    """
    Display a navigation menu
    Option 1 creates a new task
    Option 2 displays a list of all tasks and deletes the one selected from the list
    """
    print("\nMenu")
    for key, value in menu.items():
        print("{}. {}".format(key, value))

    selected_option = input("\nSelect an option: ")
    try:
        selected_option = int(selected_option)
        if selected_option == 1:
            task = input("\nEnter your task: ")
            print("[+] Creating your task...")
            time.sleep(2)
            create_task(task)
            print("[+] Task created successfully\n")
            main()

        if selected_option == 2:
            print("\nYour Tasks")
            for i, item in enumerate(todo_list):
                print("{}. {}".format(i+1, item))
            selected_task = input("\nSelect a task to delete: ")
            print("[+] Deleting task...")
            time.sleep(2)
            delete_task(todo_list[int(selected_task) - 1])
            print("[+] Task has been deleted successfully\n")
            main()

        if selected_option == 3:
            print("\n[+] Deleting all tasks...")
            time.sleep(2)
            delete_all_tasks()
            print("[+] Tasks have been deleted successfully\n")
            main()

        if selected_option == 4:
            print("\nYour Tasks")
            for i, item in enumerate(todo_list):
                print("{}. {}".format(i+1, item))
            selected_task = input("\nSelect a finished task: ")
            print("[+] Marking task as finished...")
            time.sleep(2)
            mark_as_finished(todo_list[int(selected_task) - 1])
            print("[+] Task has been marked successfully\n")

        if selected_option == 5:
            print("\nYour Tasks")
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

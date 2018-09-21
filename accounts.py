accounts = {}


def add_account(name, password):
    """
    Adds a user to the accounts dictionary
    with password as key and name as value
    """

    #  Check for blank username and password
    if not name and not password:
        return "Blank name or password", False

    #  Check if user already exists
    if accounts.get(password):
        return "User already exists", False

    #  Add a new user
    accounts.update({name: password})
    return True


def login(name, password):
    """
    Returns True if the name and the corresponding password 
    exists in the accounts dictionary
    """

    #  Check if user account exists
    if accounts.get(password) == name:
        return True
    return False

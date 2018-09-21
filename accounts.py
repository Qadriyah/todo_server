accounts = {}


def add_account(name, password):
    """
    Adds a user to the accounts dictionary with password 
    as key and name as value. Returns a tuple with two
    elements, a boolean and a message

    Arguments:
    name        -- the name that will be used by the user to login.
    password    -- the password that will be used during authentication
    """

    #  Check for blank username and password
    if not name and not password:
        return "Blank name or password", False

    #  Check if user already exists
    if accounts.get(password):
        return "User already exists", False

    #  Add a new user
    accounts.update({name: password})
    return "Sucess", True


def login(name, password):
    """
    Checks if the name and the corresponding password 
    exists in the accounts dictionary and returns a boolean

    Arguments:
    name        -- username
    password    -- user password
    """

    #  Check if user account exists
    if accounts.get(password) == name:
        return True
    return False

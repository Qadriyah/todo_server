accounts = {}


def add_account(name, password):
    """
    Adds a user to the accounts dictionary
    with password as key and name as value
    """

    if not name and not password:
        return "Blank name or password", False
    accounts.update({name: password})


def login(name, password):
    """
    Returns True if the name and the corresponding password 
    exists in the accounts dictionary
    """

    if accounts.get(password):
        if accounts[password] is name:
            return True
        return False
    return False

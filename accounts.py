accounts = {}


def add_account(name, password):
    """
    Adds a user to the accounts dictionary
    with password as key and name as value
    """

    if not name and not password:
        return "Blank name or password", False
    accounts.update({name: password})

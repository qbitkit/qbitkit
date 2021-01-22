def remove_value(self=list([]), value=None):
    """Removes a specified value from a specified list, and returns a list without the specified value included.

    Args:
        self(list): A list to remove values from. (default list([]))
        value(*): Value to remove from list. Can be any value. (default None)
    Returns:
        list: List with specified values removed."""
    return [value for value in self if value]

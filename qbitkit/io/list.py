def fill_range(fill=str('m'),
               iterations=int(10),
               append=None):
    """Fill a list with value fill repeated a specified number of times.

    Args:
        fill(str): String to repeat. (default str('m'))
        iterations(int): Number of times to repeat string. (default int(10))
        append(list): List to append generated list to. If None, does not append to a list. (default None)
    Return:
        list: Generated list."""
    if type(append) != list:
        append = []
    for iteration in range(iterations):
        append.append(fill)
    return append

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

def count_range(start=int(0),
                end=int(9),
                append=None):
    """Count between values start and end, appending each value to a list.

    Args:
        start(int): Number to start counting at. (default int(0))
        end(int): Number to stop counting at. (default int(9))
        append(list): List to append generated list to, if set to None function will not append to anything. (default None)
    Returns:
        list: Generated list.
    """

    specified_range = range(int(start),
                            int(end))

    if append is None:
        generated_list = list([])
    else:
        generated_list = append

    for iteration in specified_range:
        generated_list.append(int(iteration))

    return generated_list
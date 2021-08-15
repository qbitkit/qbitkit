def fill_range(fill=str('m'),
               iterations=int(10)):
    """Fill a list with value fill repeated a specified number of times.

    Args:
        fill(str): String to repeat. (default str('m'))
        iterations(int): Number of times to repeat string. (default int(10))
        append(list): List to append generated list to. If None, does not append to a list. (default None)
    Return:
        list: Generated list."""
    append = []
    for iteration in range(iterations):
        append.append(fill)
    return append


def count_range(start=int(0),
                end=int(9)):
    """Count between values start and end, appending each value to a list.

    Args:
        start(int): Number to start counting at. (default int(0))
        end(int): Number to stop counting at. (default int(9))
    Returns:
        list: Generated list.
    """
    
    specified_range = range(int(start),
                            int(end))
    
    generated_list = [int(i) for i in specified_range]

    return generated_list


def count(lst=None):
    """Count items in a specified list.

    Args:
        lst(list): The list to count items from. (default None)
    Returns:
        int: Count of items in specified list."""
    # Initialize Variables
    lst = list(lst)
    item_count = 0

    # Iterate over specified list
    for item in lst:
        # Add 1 to item counter for each item in the list
        item_count = item_count + 1

    # Return the number of items in the specified list
    return item_count

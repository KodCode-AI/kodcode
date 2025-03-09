def is_ascending(lst):
    """
    Returns True if the list is sorted in ascending order, otherwise False.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
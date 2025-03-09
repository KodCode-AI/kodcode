def is_sorted_ascending(numbers_list):
    """
    Returns True if the list is sorted in ascending order, otherwise False.
    """
    return all(numbers_list[i] <= numbers_list[i + 1] for i in range(len(numbers_list) - 1))
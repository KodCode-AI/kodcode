def is_sorted_ascending(numbers):
    """
    Returns True if the list of numbers is sorted in ascending order, else False.
    """
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
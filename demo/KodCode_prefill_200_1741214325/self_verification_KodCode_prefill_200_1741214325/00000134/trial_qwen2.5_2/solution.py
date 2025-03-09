def second_smallest(numbers):
    """
    Finds the second smallest number in a list.
    Returns None if there are less than two unique numbers.
    """
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    else:
        return sorted(unique_numbers)[1]
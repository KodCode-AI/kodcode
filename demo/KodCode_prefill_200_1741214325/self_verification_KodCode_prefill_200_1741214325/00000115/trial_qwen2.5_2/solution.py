def find_max(numbers):
    """
    Returns the maximum number from a list of numbers.
    """
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty.")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
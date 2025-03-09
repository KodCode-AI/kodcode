def find_max(numbers):
    """
    Returns the maximum number in a list of numbers.
    
    Args:
    numbers (list): A list of numbers.
    
    Returns:
    int or float: The maximum number in the list.
    """
    if not numbers:
        raise ValueError("The list is empty")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
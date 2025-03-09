def sum_recursive(numbers):
    """
    Calculate the sum of all numbers in a list using recursion.
    
    Args:
        numbers (list): A list of integers or floats.
    
    Returns:
        int or float: The sum of all numbers in the list.
    """
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])
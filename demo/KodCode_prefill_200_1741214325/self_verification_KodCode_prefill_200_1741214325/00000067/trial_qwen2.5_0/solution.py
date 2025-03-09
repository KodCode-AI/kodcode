def sum_of_evens(numbers):
    """
    Returns the sum of all even numbers in the given list.
    
    Example:
    - Given [1, 2, 3, 4, 5, 6], it should return 12 (2 + 4 + 6 = 12).
    """
    return sum([num for num in numbers if num % 2 == 0])
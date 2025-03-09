def sum_of_evens(numbers):
    """
    Returns the sum of all even numbers in the given list.
    """
    return sum(num for num in numbers if num % 2 == 0)
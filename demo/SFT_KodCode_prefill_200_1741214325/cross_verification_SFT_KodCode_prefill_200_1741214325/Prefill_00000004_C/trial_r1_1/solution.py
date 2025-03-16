def sum_recursive(numbers):
    """Calculate the sum of all numbers in a list using recursion."""
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])
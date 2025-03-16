def sum_recursive(numbers):
    if not numbers:  # Base case: empty list
        return 0
    else:  # Recursive case: add first element to sum of the rest
        return numbers[0] + recursive_sum(numbers[1:])
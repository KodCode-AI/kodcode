def sum_recursive(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])
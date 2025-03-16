def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Sum:", recursive_sum(numbers))  # Output: Sum: 15
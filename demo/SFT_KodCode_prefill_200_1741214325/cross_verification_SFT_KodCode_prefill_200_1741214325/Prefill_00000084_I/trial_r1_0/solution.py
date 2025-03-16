def count_value_occurrences(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count

# Example usage:
sample_list = [1, 2, 3, 4, 5, 2, 2, 3]
print(count_occurrences(sample_list, 2))  # Output: 3
print(count_occurrences(sample_list, 5))  # Output: 1
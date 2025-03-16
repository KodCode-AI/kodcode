def are_elements_unique(array):
    # Convert the array into a set to eliminate duplicates
    unique_elements = set(array)
    # Compare the lengths: if equal, all elements were unique
    return len(array) == len(unique_elements)

# Example usage:
# print(all_unique_elements([1, 2, 3, 4]))  # Output: True
# print(all_unique_elements([1, 2, 2, 3]))  # Output: False
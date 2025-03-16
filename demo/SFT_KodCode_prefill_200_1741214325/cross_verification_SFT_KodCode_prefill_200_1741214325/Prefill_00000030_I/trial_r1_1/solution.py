def are_elements_unique(arr):
    # Convert the array to a set, which automatically removes duplicates
    unique_elements = set(arr)
    # Compare the lengths of the original array and the set
    # If they are the same, all elements were unique
    return len(arr) == len(unique_elements)
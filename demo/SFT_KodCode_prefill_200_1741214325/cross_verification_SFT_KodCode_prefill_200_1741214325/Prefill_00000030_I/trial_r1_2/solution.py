def are_elements_unique(array):
    # Convert the array to a set to remove duplicates
    # If the lengths are equal, all elements are unique
    return len(array) == len(set(array))
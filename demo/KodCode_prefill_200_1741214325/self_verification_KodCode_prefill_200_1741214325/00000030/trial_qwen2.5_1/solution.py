def are_elements_unique(arr):
    """
    Determines if all elements in the array are unique.

    Arguments:
    arr -- list of elements

    Returns:
    bool -- True if all elements are unique, False otherwise.
    """
    # Convert the list to a set and compare its length to the original list's length
    return len(arr) == len(set(arr))
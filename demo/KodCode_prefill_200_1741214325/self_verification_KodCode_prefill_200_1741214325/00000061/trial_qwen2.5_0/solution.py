def find_first_unique(arr):
    """
    Returns the first index of the element that is not repeated in the array.
    If no such element exists, returns -1.
    """
    element_count = {}
    
    # Count the occurrences of each element
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # Find the first element with a count of 1
    for i, element in enumerate(arr):
        if element_count[element] == 1:
            return i
    
    return -1
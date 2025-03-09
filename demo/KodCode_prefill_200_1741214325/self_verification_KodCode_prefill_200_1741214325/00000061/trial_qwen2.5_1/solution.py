def find_unique_element(arr):
    """
    Returns the index of the first unique element in the given array.
    If no unique element is found, returns -1.
    """
    element_counts = {}
    
    # Count occurrences of each element
    for i, num in enumerate(arr):
        if num in element_counts:
            element_counts[num] += 1
        else:
            element_counts[num] = 1
    
    # Find the first unique element's index
    for i, num in enumerate(arr):
        if element_counts[num] == 1:
            return i
    
    return -1
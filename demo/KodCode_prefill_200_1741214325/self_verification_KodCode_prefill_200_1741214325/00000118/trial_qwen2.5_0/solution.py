def find_minimum(lst):
    """
    Returns the minimum element in the given list.
    """
    if not lst:  # check if the list is empty
        return None
    
    min_element = lst[0]
    for element in lst[1:]:
        if element < min_element:
            min_element = element
            
    return min_element
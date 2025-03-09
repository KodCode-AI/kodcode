def find_min_element(lst):
    """
    Returns the minimum element in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    The minimum element in the list.
    """
    if not lst:  # Check if the list is empty
        return None
    min_element = lst[0]
    for element in lst[1:]:
        if element < min_element:
            min_element = element
    return min_element
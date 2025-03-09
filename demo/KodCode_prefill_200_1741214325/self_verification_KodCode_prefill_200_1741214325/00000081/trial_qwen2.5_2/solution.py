def count_unique_elements(lst):
    """
    Returns the number of unique elements in a given list.
    
    Parameters:
    lst (list): The input list containing elements.
    
    Returns:
    int: The number of unique elements.
    """
    unique_elements = set(lst)
    return len(unique_elements)
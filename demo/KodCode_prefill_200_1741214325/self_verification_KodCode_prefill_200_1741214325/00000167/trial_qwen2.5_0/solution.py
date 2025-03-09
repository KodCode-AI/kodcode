def count_missing_data(nested_list):
    """
    Counts the number of missing data (None) in a nested list.
    
    Parameters:
    nested_list (list): A nested list containing any type of elements.
    
    Returns:
    int: The count of missing data (None) in the nested list.
    """
    count = 0
    for element in nested_list:
        if element is None:
            count += 1
        elif isinstance(element, list):
            count += count_missing_data(element)
    return count
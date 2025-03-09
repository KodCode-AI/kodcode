def remove_duplicates(lst):
    """
    Returns a new list with duplicates removed while preserving the original order.
    
    Args:
    lst (list): The input list which may contain duplicate elements.
    
    Returns:
    list: A list with unique elements.
    """
    unique_elements = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_elements.append(item)
            seen.add(item)
    return unique_elements
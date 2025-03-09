def union_of_lists(list1, list2):
    """
    Returns the union of elements in two lists.
    
    Args:
    list1: First input list.
    list2: Second input list.
    
    Returns:
    A list containing the union of the two input lists, without duplicates.
    """
    return list(set(list1 + list2))
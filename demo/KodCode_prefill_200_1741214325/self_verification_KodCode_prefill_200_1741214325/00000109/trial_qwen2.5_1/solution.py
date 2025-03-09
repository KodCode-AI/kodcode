def find_common_elements(list1, list2):
    """
    Returns a new list containing the common elements between two input lists.
    """
    return list(set(list1) & set(list2))
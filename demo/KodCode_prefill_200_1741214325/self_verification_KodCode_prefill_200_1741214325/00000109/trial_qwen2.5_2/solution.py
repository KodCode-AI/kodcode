def find_common_elements(list1, list2):
    """
    Returns a new list containing elements common to both input lists.
    """
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)
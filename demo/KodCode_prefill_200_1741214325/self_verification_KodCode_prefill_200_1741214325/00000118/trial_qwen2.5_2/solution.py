def find_minimum(lst):
    """
    Returns the minimum element from the provided list.
    """
    if not lst:
        raise ValueError("List is empty")
    min_element = lst[0]
    for element in lst:
        if element < min_element:
            min_element = element
    return min_element
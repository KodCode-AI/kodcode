def remove_duplicates_preserve_order(lst):
    """
    Removes duplicates from a list while preserving the original order of elements.
    
    :param lst: List from which duplicates are to be removed.
    :return: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
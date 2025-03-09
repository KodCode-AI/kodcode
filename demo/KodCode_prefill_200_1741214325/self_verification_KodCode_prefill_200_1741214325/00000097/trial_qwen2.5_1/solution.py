def remove_duplicates_preserve_order(input_list):
    """
    Removes duplicates from a list while preserving the original order of elements.
    
    :param input_list: List from which to remove duplicates.
    :return: A new list with duplicates removed and original order preserved.
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
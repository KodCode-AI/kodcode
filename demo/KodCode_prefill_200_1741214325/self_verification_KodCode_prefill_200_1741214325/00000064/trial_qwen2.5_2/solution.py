def remove_duplicates(input_list):
    """
    Returns a new list with duplicates removed while preserving the original order.
    """
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
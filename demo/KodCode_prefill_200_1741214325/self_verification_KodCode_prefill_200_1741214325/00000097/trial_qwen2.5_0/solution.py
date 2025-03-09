def remove_duplicates_preserve_order(items):
    """
    Removes duplicates from a list while preserving the original order of elements.
    Args:
    items (list): The list from which to remove duplicates.
    
    Returns:
    list: A new list with duplicates removed and original order preserved.
    """
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items
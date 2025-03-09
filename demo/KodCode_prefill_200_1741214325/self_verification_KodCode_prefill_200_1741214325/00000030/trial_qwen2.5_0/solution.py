def are_elements_unique(arr):
    """
    Check if all elements in the given array are unique.
    
    This function uses a set to track seen elements. If an element is encountered that
    is already in the set, it means the element is not unique, and the function returns False.
    Otherwise, if the loop completes without finding any duplicates, the function returns True.
    """
    seen = set()
    for element in arr:
        if element in seen:
            return False
        seen.add(element)
    return True
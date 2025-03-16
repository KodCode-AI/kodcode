from typing import List

def find_min_element(lst: List[int]) -> int:
    """ Returns the minimum element in the list lst.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        The minimum element in the list. Returns None if the list is empty.
    """
    if not lst:
        return None
    return min(lst)
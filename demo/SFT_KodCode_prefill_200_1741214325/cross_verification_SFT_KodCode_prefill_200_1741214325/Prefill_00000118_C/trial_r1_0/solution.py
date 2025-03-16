from typing import List

def find_min_element(strs: List[int]) -> int:
    """ Returns the minimum element in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    The minimum element in the list.
    """
    if not strs:  # Check if the list is empty
        return None
    min_element = strs[0]
    for element in strs[1:]:
        if element < min_element:
            min_element = element
    return min_element
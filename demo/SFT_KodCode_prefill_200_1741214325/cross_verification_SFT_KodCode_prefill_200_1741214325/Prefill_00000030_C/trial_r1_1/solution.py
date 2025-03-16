from typing import List

def are_elements_unique(arr: List[int]) -> bool:
    """
    Returns True if all elements in the array are unique, otherwise returns False.
    
    Parameters:
    arr (list): The input list of elements
    
    Returns:
    bool: True if all elements are unique, False otherwise
    """
    return len(arr) == len(set(arr))
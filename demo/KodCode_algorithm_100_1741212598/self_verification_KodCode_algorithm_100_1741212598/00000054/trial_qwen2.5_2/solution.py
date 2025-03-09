from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    """
    Returns the peak element in a unimodal list. If the list does not follow the unimodal pattern, returns None.
    """
    if not lst:
        return None
    
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < lst[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return lst[left]
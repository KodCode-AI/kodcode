from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    """
    Returns the peak element in a unimodal list.
    If the list is not unimodal, returns None.
    """
    left, right = 0, len(lst) - 1
    
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < lst[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return lst[left] if left < len(lst) and lst[left] >= lst[(left - 1) % len(lst)] else None
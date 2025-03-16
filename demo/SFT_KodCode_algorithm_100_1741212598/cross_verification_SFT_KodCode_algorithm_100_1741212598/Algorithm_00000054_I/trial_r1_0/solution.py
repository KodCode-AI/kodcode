from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    if not lst:
        return None  # According to constraints, len(lst) >= 1, so this might be redundant
    
    max_val = max(lst)
    first_max = lst.index(max_val)
    reversed_max_index = lst[::-1].index(max_val)
    last_max = len(lst) - 1 - reversed_max_index
    
    # Check non-decreasing from start to first_max (exclusive)
    for i in range(first_max):
        if lst[i] > lst[i + 1]:
            return None
    
    # Check non-increasing from last_max (inclusive) to end
    for i in range(last_max, len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return None
    
    # Check all elements from first_max to last_max are max_val
    for i in range(first_max, last_max + 1):
        if lst[i] != max_val:
            return None
    
    return max_val
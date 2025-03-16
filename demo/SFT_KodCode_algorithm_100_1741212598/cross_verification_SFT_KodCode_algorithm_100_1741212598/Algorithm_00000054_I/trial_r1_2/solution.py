from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    if not lst:
        return None
    max_val = max(lst)
    first_peak = lst.index(max_val)
    last_peak = len(lst) - 1 - lst[::-1].index(max_val)
    
    # Check non-decreasing from start to first_peak
    for i in range(first_peak):
        if lst[i] > lst[i + 1]:
            return None
    
    # Check all elements between first_peak and last_peak are max_val
    for i in range(first_peak, last_peak + 1):
        if lst[i] != max_val:
            return None
    
    # Check non-increasing from last_peak to end
    for i in range(last_peak, len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return None
    
    return max_val
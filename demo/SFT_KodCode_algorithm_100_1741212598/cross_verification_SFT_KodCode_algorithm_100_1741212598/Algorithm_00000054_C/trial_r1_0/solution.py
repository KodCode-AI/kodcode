from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            # Check if all elements before i are strictly increasing
            is_increasing = True
            for j in range(i - 1):
                if lst[j] >= lst[j + 1]:
                    is_increasing = False
                    break
            if not is_increasing:
                continue
            
            # Check if all elements after i are strictly decreasing
            is_decreasing = True
            for j in range(i, len(lst) - 1):
                if lst[j] <= lst[j + 1]:
                    is_decreasing = False
                    break
            if is_decreasing:
                return lst[i]
    
    return None
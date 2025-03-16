from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    
    peak_idx = -1
    phase = 'prerise'  # either 'prerise' or 'postpeak'
    
    for i in range(len(lst) - 1):
        current = lst[i]
        next_elem = lst[i + 1]
        
        if phase == 'prerise':
            if next_elem > current:
                continue
            elif next_elem == current:
                continue  # plateau is allowed in non-decreasing phase
            else:  # next_elem < current
                phase = 'postpeak'
                peak_idx = i
        else:  # phase is 'postpeak'
            if next_elem > current:
                return None  # increasing after postpeak, invalid
    
    # After the loop, check if a peak was found
    if peak_idx != -1:
        return lst[peak_idx]
    else:
        # Check if all elements are the same
        first = lst[0]
        all_same = all(x == first for x in lst)
        if all_same:
            return first
        else:
            return None
from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    if not lst:
        return None  # Though per constraints, len >=1, so this might be unnecessary.
    n = len(lst)
    if n == 1:
        return lst[0]
    
    # Compute left_incr: True if the subarray lst[0..i] is non-decreasing
    left_incr = [False] * n
    left_incr[0] = True
    for i in range(1, n):
        if lst[i] >= lst[i-1] and left_incr[i-1]:
            left_incr[i] = True
        else:
            left_incr[i] = False
    
    # Compute right_decr: True if the subarray lst[i..n-1] is non-increasing
    right_decr = [False] * n
    right_decr[-1] = True
    for i in range(n-2, -1, -1):
        if lst[i] >= lst[i+1] and right_decr[i+1]:
            right_decr[i] = True
        else:
            right_decr[i] = False
    
    max_val = max(lst)
    max_indices = [i for i, x in enumerate(lst) if x == max_val]
    
    for i in max_indices:
        if left_incr[i] and right_decr[i]:
            return max_val
    return None
from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    """ Returns the maximum sum of a contiguous subarray within the one-dimensional array of numbers."""
    if not arr:
        return 0
    
    current_max = global_max = arr[0]
    
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    
    return global_max
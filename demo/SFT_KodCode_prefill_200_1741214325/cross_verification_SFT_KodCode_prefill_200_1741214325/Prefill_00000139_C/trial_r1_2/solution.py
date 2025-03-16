from typing import List

def max_subarray_kadane(arr: List[int]) -> int:
    if not arr:
        return 0  # Return 0 for an empty array, assuming it's a valid case
    
    current_max = global_max = arr[0]
    
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    
    return global_max
from typing import List

def max_subarray_kadane(arr: List[int]) -> int:
    current_max = global_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)
    return global_max
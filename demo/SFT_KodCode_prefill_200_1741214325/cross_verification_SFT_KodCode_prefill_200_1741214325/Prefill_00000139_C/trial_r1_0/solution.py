from typing import List

def max_subarray_kadane(arr: List[int]) -> int:
    if not arr:
        return 0  # Return 0 for empty array
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global
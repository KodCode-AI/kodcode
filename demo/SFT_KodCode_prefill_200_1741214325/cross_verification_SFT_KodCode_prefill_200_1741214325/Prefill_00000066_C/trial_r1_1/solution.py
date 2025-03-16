from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    if not arr:
        return 0
    max_so_far = current_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        if current_max > max_so_far:
            max_so_far = current_max
    return max_so_far
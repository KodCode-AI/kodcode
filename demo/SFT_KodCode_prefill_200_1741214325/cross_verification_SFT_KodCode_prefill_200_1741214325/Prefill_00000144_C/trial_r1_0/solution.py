from typing import List

def max_triplet_product(arr: List[int]) -> int:
    if len(arr) < 3:
        raise ValueError("The input array must contain at least three elements.")
    sorted_arr = sorted(arr)
    candidate1 = sorted_arr[-1] * sorted_arr[-2] * sorted_arr[-3]
    candidate2 = sorted_arr[0] * sorted_arr[1] * sorted_arr[-1]
    return max(candidate1, candidate2)
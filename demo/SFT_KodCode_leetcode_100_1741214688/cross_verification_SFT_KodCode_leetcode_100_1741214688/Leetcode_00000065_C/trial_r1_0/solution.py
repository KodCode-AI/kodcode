from typing import List

def find_missing_element(nums: List[int]) -> int:
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
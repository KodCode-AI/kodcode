from typing import List

def find_missing_element(nums: List[int]) -> int:
    m = len(nums) + 1
    expected_sum = m * (m + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
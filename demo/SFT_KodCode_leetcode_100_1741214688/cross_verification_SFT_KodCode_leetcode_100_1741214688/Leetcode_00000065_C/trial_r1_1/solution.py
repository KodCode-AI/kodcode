from typing import List

def find_missing_element(nums: List[int]) -> int:
    sum_nums = sum(nums)
    m = len(nums) + 1
    expected_sum = m * (m + 1) // 2
    return expected_sum - sum_nums
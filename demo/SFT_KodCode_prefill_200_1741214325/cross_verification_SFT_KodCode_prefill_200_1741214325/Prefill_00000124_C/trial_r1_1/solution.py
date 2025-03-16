from typing import List

def single_number(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res
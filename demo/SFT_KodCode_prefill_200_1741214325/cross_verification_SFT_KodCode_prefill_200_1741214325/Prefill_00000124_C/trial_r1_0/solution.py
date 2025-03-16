from typing import List

def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
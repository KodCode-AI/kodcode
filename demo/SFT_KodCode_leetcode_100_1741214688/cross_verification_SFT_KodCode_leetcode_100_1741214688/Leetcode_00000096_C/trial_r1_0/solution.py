from typing import List

def find_pair_with_sum(nums: List[int], k: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = k - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
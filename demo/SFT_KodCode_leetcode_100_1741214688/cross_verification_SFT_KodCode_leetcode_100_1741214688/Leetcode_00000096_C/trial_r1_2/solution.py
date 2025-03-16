from typing import List

def find_pair_with_sum(nums: List[int], k: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        target = k - num
        if target in seen:
            return [seen[target], i]
        seen[num] = i
    return []
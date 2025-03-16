from typing import List

def two_sum_indices(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        return []
    sorted_nums = sorted([(val, idx) for idx, val in enumerate(nums)], key=lambda x: x[0])
    left = 0
    right = len(sorted_nums) - 1
    while left < right:
        current_sum = sorted_nums[left][0] + sorted_nums[right][0]
        if current_sum == target:
            return [sorted_nums[left][1], sorted_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
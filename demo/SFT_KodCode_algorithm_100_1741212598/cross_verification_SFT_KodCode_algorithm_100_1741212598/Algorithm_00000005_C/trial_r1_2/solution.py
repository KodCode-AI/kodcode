from typing import List

def two_sum_indices(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        return []
    
    sorted_pairs = sorted(((num, idx) for idx, num in enumerate(nums)), key=lambda x: x[0])
    left = 0
    right = len(sorted_pairs) - 1
    
    while left < right:
        current_sum = sorted_pairs[left][0] + sorted_pairs[right][0]
        if current_sum == target:
            return [sorted_pairs[left][1], sorted_pairs[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
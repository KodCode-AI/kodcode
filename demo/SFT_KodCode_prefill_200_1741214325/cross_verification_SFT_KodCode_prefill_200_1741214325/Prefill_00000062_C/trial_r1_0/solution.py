from typing import List

def second_maximum(numbers: List[int]) -> int:
    unique_nums = list(set(numbers))
    unique_nums.sort(reverse=True)
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]
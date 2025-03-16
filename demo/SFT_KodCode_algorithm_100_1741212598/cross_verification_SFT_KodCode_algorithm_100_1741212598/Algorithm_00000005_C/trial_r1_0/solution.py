from typing import List

def two_sum_indices(nums: List[int], target: int) -> List[int]:
    # Create a list of tuples with value and original index
    indexed = [(val, idx) for idx, val in enumerate(nums)]
    # Sort the list based on the values
    indexed.sort(key=lambda x: x[0])
    
    left = 0
    right = len(indexed) - 1
    
    while left < right:
        current_sum = indexed[left][0] + indexed[right][0]
        if current_sum == target:
            # Get the original indices and sort them before returning
            res = [indexed[left][1], indexed[right][1]]
            res.sort()
            return res
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    # Return empty list if no pair is found
    return []
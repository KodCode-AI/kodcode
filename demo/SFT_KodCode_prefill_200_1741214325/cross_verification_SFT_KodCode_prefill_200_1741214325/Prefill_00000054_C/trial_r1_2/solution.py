from typing import List

def max_product_subarray(nums: List[int]) -> int:
    """
    Returns the maximum product of a contiguous subarray within the one-dimensional array of numbers.
    """
    if not nums:
        return 0
    
    # Initialize local minimum, local maximum, and the answer with the first element.
    local_min, local_max, ans = nums[0], nums[0], nums[0]
    
    for num in nums[1:]:
        # If the current number is negative, swap the local min and max.
        if num < 0:
            local_min, local_max = local_max, local_min
        
        # Update the local max and min.
        local_max = max(num, local_max * num)
        local_min = min(num, local_min * num)
        
        # Update the answer.
        ans = max(ans, local_max)
    
    return ans
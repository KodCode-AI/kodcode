from typing import List

def max_product_subarray(nums: List[int]) -> int:
    if not nums:
        return 0
    
    local_min = local_max = ans = nums[0]
    
    for num in nums[1:]:
        # Consider all possibilities to update local_max and local_min
        temp_max = max(num, local_max * num, local_min * num)
        temp_min = min(num, local_max * num, local_min * num)
        
        # Update the local_min and local_max for the next iteration
        local_max, local_min = temp_max, temp_min
        
        # Track the maximum answer
        ans = max(ans, local_max)
    
    return ans
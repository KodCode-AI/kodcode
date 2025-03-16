from typing import List

def max_product_subarray(nums: List[int]) -> int:
    if not nums:
        return 0
    
    local_min = local_max = ans = nums[0]
    
    for num in nums[1:]:
        # Calculate the potential new local_max and local_min
        temp_max = max(num, num * local_max, num * local_min)
        temp_min = min(num, num * local_max, num * local_min)
        
        # Update the local_min and local_max for the next iteration
        local_max, local_min = temp_max, temp_min
        
        # Update the answer if a larger product is found
        ans = max(ans, local_max)
    
    return ans
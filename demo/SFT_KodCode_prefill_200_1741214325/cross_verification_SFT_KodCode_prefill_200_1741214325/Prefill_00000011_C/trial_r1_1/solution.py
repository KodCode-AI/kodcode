from typing import List

def max_product_subarray(nums: List[int]) -> int:
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        # Calculate possible new max and min products
        temp_max = max(num, max_product * num, min_product * num)
        temp_min = min(num, max_product * num, min_product * num)
        
        # Update max and min for next iteration
        max_product, min_product = temp_max, temp_min
        
        # Update result if current max is larger
        result = max(result, max_product)
    
    return result
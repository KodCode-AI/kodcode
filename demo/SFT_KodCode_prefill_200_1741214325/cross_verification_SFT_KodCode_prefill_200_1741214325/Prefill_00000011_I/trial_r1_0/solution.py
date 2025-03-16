def max_product_subarray(nums):
    if not nums:
        return None  # or raise ValueError("Array is empty")
    
    max_p = min_p = result = nums[0]
    
    for num in nums[1:]:
        temp_max1 = max_p * num
        temp_max2 = min_p * num
        temp_min1 = max_p * num
        temp_min2 = min_p * num
        
        new_max = max(num, temp_max1, temp_max2)
        new_min = min(num, temp_min1, temp_min2)
        
        max_p, min_p = new_max, new_min
        
        if max_p > result:
            result = max_p
            
    return result
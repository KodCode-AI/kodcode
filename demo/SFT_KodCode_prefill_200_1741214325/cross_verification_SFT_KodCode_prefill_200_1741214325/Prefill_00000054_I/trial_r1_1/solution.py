def max_product_subarray(nums):
    if not nums:
        return 0  # Assuming default return value for empty array as 0
    
    current_max = current_min = global_max = nums[0]
    
    for num in nums[1:]:
        # Calculate potential new max and min
        temp_max = max(num, current_max * num, current_min * num)
        temp_min = min(num, current_max * num, current_min * num)
        
        # Update current_max and current_min
        current_max, current_min = temp_max, temp_min
        
        # Update global_max if current_max is larger
        if current_max > global_max:
            global_max = current_max
    
    return global_max
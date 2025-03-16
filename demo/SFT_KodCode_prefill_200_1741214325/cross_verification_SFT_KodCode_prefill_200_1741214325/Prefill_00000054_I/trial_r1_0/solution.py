def max_product_subarray(nums):
    if not nums:
        return 0  # Handle empty array case, though problem states it's one-dimensional, so it may not be necessary.
    max_p = min_p = global_max = nums[0]
    
    for num in nums[1:]:
        temp1 = num * max_p
        temp2 = num * min_p
        current = num
        
        new_max = max(current, temp1, temp2)
        new_min = min(current, temp1, temp2)
        
        max_p, min_p = new_max, new_min
        
        if new_max > global_max:
            global_max = new_max
    
    return global_max
def max_product_subarray(nums):
    """
    Returns the maximum product of a subarray within the given array of integers.
    """
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        temp_max = max(num, max_product * num, min_product * num)
        min_product = min(num, max_product * num, min_product * num)
        max_product = temp_max
        
        result = max(result, max_product)
        
    return result
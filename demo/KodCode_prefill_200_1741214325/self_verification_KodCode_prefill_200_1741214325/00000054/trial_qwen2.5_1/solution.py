def max_product_subarray(nums):
    """
    Returns the maximum product of a contiguous subarray within nums.
    """
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        # The maximum product can be updated using the current number, max_product, or min_product
        candidates = (num, max_product * num, min_product * num)
        max_product = max(candidates)
        min_product = min(candidates)
        
        # Update the result with the maximum product found so far
        result = max(result, max_product)
    
    return result
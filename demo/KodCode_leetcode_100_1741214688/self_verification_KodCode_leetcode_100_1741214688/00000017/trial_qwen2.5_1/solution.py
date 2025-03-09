def max_consecutive_ones(nums, k):
    """
    Returns the maximum number of consecutive 1's in the array if you can flip at most k 0's to 1's.
    """
    left = 0
    max_ones = 0
    zero_count = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_ones = max(max_ones, right - left + 1)
    
    return max_ones
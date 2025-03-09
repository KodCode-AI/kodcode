def max_subarray_sum(nums, k):
    """
    Return the maximum sum of a non-empty subarray of size k that contains at least one negative number.
    If no such subarray exists, return 0.
    """
    n = len(nums)
    if n < k or k <= 0:
        return 0
    
    max_sum = float('-inf')
    current_sum = 0
    has_negative = False
    
    for i in range(n):
        current_sum += nums[i]
        if nums[i] < 0:
            has_negative = True
        
        if i >= k - 1:
            if has_negative:
                max_sum = max(max_sum, current_sum)
            current_sum -= nums[i - k + 1]
            if nums[i - k + 1] < 0:
                has_negative = False
    
    return max(max_sum, 0) if max_sum != float('-inf') else 0
def max_subarray_sum(nums, k):
    """
    Returns the maximum sum of a non-empty subarray of size k that contains at least one negative number.
    If there is no such subarray, returns 0.
    """
    if len(nums) < k or k == 0:
        return 0
    
    max_sum = float('-inf')
    current_sum = 0
    negative_included = False
    for i in range(len(nums)):
        current_sum += nums[i]
        if nums[i] < 0:
            negative_included = True
        if i >= k - 1:
            if negative_included and current_sum > max_sum:
                max_sum = current_sum
            if nums[i - k + 1] < 0:
                negative_included = False
            current_sum -= nums[i - k + 1]
    
    return max_sum if max_sum != float('-inf') else 0
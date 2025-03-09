def max_subarray_sum_with_negative(nums, k):
    """
    Returns the maximum sum of a non-empty subarray of size k that contains at least one negative number.
    If there is no such subarray, returns 0.
    """
    n = len(nums)
    max_sum = float('-inf')
    for i in range(n - k + 1):
        current_sum = sum(nums[i:i+k])
        has_negative = any(num < 0 for num in nums[i:i+k])
        if has_negative:
            max_sum = max(max_sum, current_sum)
    return max_sum if max_sum != float('-inf') else 0
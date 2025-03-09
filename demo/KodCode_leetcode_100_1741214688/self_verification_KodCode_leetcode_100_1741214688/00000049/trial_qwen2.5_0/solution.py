def shortest_subarray_with_sum_at_least_target(nums, target):
    """
    Finds the shortest contiguous subarray in nums such that the sum of the
    elements in the subarray is equal to or greater than target. Returns 0 if
    no such subarray exists.
    """
    n = len(nums)
    if n < 2:
        return 0
    
    shortest_length = float('inf')
    left = 0
    current_sum = 0
    
    for right in range(n):
        current_sum += nums[right]
        
        while current_sum >= target:
            shortest_length = min(shortest_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return shortest_length if shortest_length != float('inf') else 0
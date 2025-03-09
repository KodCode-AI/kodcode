def shortest_subarray_with_at_least_sum(nums, target):
    """
    Finds the shortest contiguous subarray in `nums` such that the sum of the elements in the subarray is 
    equal to or greater than `target`. If no such subarray exists, returns 0.
    """
    n = len(nums)
    start, end = 0, 0
    current_sum = 0
    min_length = float('inf')
    
    while end < n:
        while current_sum < target and end < n:
            current_sum += nums[end]
            end += 1
        
        while current_sum >= target and start < n:
            min_length = min(min_length, end - start)
            current_sum -= nums[start]
            start += 1
    
    return min_length if min_length != float('inf') else 0
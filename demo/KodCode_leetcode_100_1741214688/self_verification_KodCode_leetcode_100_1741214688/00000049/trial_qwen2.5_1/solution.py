def shortest_subarray_with_target(nums, target):
    """
    Returns the length of the shortest contiguous subarray in nums
    such that the sum of the elements in the subarray is equal to or greater than target.
    If no such subarray exists, return 0.
    """
    n = len(nums)
    if n < 2:
        return 0
    
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += nums[end]
        
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
            
    return min_length if min_length != float('inf') else 0
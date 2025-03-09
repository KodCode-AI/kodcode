def calculate_result(nums):
    """
    Returns a result array where result[i] is the sum of f(nums[i]) for all i in the array.
    """
    from bisect import bisect_left
    
    sorted_nums = sorted(set(nums))  # Get unique and sorted elements
    index_map = {val: idx for idx, val in enumerate(sorted_nums)}
    prefix_sum = [0]
    for num in sorted_nums:
        prefix_sum.append(prefix_sum[-1] + bisect_left(sorted_nums, num))
    
    result = []
    for num in nums:
        idx = index_map[num]
        result.append(sum(prefix_sum[:idx]))
    return result
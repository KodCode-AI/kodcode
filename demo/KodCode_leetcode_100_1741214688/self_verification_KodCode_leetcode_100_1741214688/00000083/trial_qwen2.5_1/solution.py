def k_smallest_abs_differences(nums, k):
    """
    Returns the k smallest absolute differences between any two distinct
    elements in the list nums. The output is unique and sorted in ascending order.
    """
    nums.sort()
    abs_diffs = {}
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if diff not in abs_diffs:
                abs_diffs[diff] = 1
            else:
                abs_diffs[diff] += 1
            
            # If we have found k unique differences, stop early
            if len(abs_diffs) == k:
                return sorted(abs_diffs.keys())[:k]
    
    # If there are fewer than k unique differences, return all of them
    return sorted(abs_diffs.keys())
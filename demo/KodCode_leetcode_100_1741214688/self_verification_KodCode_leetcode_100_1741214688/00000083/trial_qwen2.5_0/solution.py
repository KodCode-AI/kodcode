def k_smallest_abs_diff(nums, k):
    """
    Returns the k smallest absolute differences between any two distinct elements.
    """
    # Sort the list to simplify finding the minimum absolute differences
    nums.sort()
    differences = set()
    
    # Initialize with the smallest absolute difference
    for i in range(len(nums) - 1):
        differences.add(abs(nums[i] - nums[i + 1]))
    
    # Find other k-1 smallest absolute differences
    if k > 1:
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) - 1:
                diff = abs(nums[i] - nums[j + 1])
                if len(differences) < k and diff not in differences:
                    differences.add(diff)
                j += 1
    
    return sorted(list(differences))[:k]
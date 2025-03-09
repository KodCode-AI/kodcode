def find_k_smallest_diff(nums, k):
    """
    Returns the k smallest absolute differences between any two distinct elements in the list.
    """
    nums.sort()
    differences = set()
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            differences.add(abs(nums[i] - nums[j]))
    
    return sorted(list(differences)[:k])
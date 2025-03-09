def max_absolute_sum(nums1, nums2):
    """
    Returns the maximum possible sum of the absolute differences between corresponding elements of nums1 and nums2.
    """
    # The optimal strategy is to sort nums1 and nums2 in reverse and forward order respectively before summing their differences.
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2, reverse=True)
    return sum(abs(a - b) for a, b in zip(sorted_nums1, sorted_nums2))
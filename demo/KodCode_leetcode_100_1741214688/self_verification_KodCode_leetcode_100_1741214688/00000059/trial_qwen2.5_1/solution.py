def max_absolute_difference_sum(nums1, nums2):
    """
    Rearranges nums1 to maximize the sum of absolute differences with nums2.
    """
    nums1.sort()
    nums2.sort(reverse=True)
    max_sum = sum(abs(a - b) for a, b in zip(nums1, nums2))
    return max_sum
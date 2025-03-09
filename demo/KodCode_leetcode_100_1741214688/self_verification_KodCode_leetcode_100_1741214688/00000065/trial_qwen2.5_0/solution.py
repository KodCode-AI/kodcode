def find_missing_element(nums):
    """
    Returns the missing element in the array `nums`. The array `nums` is
    initially a sorted array of integers from `1` to `n` inclusive, where an
    element is missing, and the array is not necessarily contiguous.
    """
    expected_sum = (len(nums) + 1) * (len(nums) + 2) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
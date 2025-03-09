def wiggle_sort(nums):
    """
    Reorders the given list to achieve the wiggle sort pattern.
    """
    for i in range(1, len(nums)):
        if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums
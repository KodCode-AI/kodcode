def wiggle_sort(nums):
    """
    Perform wiggle sort on the input list.
    """
    for i in range(1, len(nums)):
        if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
            nums[i], nums[i-1] = nums[i-1], nums[i]
    return nums
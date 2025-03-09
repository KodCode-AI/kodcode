def wiggle_sort(nums):
    """
    Rearranges the elements of the input list in a wiggle pattern.
    Each element is greater or smaller than its adjacent elements.
    
    :param nums: List[int] - a list of integers
    :return: List[int] - a list of integers in a wiggle sorted order
    """
    for i in range(1, len(nums)):
        if i % 2 == 1 and nums[i] <= nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        elif i % 2 == 0 and nums[i] >= nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums
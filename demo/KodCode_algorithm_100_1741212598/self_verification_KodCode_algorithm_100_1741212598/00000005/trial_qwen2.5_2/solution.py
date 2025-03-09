def two_sum_indices(nums, target):
    """
    Finds two indices in a sorted list whose values add up to the target sum.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
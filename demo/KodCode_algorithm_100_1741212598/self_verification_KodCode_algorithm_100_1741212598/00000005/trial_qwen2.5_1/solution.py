def two_sum_indices(nums, target):
    """
    Finds the indices of the two numbers in the sorted list 'nums' that add up to 'target'.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return [left, right]
    return []
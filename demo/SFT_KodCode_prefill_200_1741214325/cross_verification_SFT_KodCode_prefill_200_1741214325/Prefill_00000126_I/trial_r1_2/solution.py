def is_sorted_ascending(nums):
    return len(nums) <= 1 or all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
def max_consecutive_ones(nums, k):
    """
    Return the maximum number of consecutive 1's in the array if you can flip at most k 0's to 1's.
    """
    left, max_len, zeros = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
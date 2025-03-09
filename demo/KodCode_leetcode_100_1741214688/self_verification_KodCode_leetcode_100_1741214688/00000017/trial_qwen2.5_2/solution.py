def max_consecutive_ones(nums, k):
    """
    Returns the maximum number of consecutive 1's in the array if you can flip at most k 0's to 1's.
    """
    max_ones = 0
    zero_count = 0
    start = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[start] == 0:
                zero_count -= 1
            start += 1

        max_ones = max(max_ones, end - start + 1)

    return max_ones
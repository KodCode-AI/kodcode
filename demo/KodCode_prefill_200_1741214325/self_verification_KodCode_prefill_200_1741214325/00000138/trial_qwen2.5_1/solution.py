def findMaxLength(nums):
    """
    Returns the length of the longest continuous subarray with equal number of 0s and 1s.
    """
    max_length = 0
    count = 0
    count_dict = {0: -1}  # Base case: subarray starting from index 0

    for i, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            count -= 1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length
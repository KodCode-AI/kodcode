def findMaxLength(nums):
    """
    Find the length of the longest continuous subarray with an equal number of 0 and 1.
    :param nums: List[int] -- List of 0s and 1s
    :return: int -- Length of the longest continuous subarray
    """
    count_map = {}
    count = 0
    max_length = 0
    count_map[0] = -1

    for i, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            count -= 1

        if count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i

    return max_length
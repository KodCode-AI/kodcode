def findMaxLength(nums):
    """
    Returns the length of the longest continuous subarray with an equal number of 0s and 1s.
    
    :param nums: List[int] - The input array of 0s and 1s.
    :return: int - Length of the longest continuous subarray with equal number of 0s and 1s.
    """
    count = 0
    count_dict = {0: -1}  # Initialize the count with 0 at index -1
    max_length = 0
    
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
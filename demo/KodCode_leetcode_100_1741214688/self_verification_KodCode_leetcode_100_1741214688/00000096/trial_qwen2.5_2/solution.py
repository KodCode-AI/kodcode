def find_pair_with_sum(nums, k):
    """
    Returns a list containing the indices of the two integers whose sum equals k.
    If no such pair exists, returns an empty list.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = k - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
def find_pair_indices(nums, k):
    """
    Determine if there exists a pair of integers in the list whose sum is equal to the target k.
    If such a pair exists, return the indices of the two integers; otherwise, return an empty list.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = k - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
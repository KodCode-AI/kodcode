def find_pair_indices(nums, k):
    """
    Given a list of n unique integers and a target integer k,
    returns the indices of the two integers in any order
    whose sum is equal to k. Returns an empty list if no such pair exists.
    
    :param nums: List[int] - A list of unique integers.
    :param k: int - The target sum.
    :return: List[int] - The indices of the pair if found, otherwise an empty list.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = k - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
def find_pair_with_sum(nums, k):
    num_dict = {}
    for index, num in enumerate(nums):
        complement = k - num
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index
    return []
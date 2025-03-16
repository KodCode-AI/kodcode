def find_pair_with_sum(nums, k):
    seen = {}
    for index, num in enumerate(nums):
        complement = k - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []
def find_pair_with_sum(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        complement = k - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
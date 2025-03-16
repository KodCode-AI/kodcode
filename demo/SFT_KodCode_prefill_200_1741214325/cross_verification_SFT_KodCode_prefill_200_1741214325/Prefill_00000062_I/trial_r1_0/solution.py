def second_maximum(nums):
    if len(nums) < 2:
        return None
    unique = set(nums)
    if len(unique) < 2:
        return None
    sorted_unique = sorted(unique, reverse=True)
    return sorted_unique[1]
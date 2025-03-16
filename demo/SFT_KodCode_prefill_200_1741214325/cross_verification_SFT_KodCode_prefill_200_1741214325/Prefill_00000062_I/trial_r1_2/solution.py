def second_maximum(nums):
    if len(nums) < 2:
        return None
    max1 = max(nums)
    filtered = [x for x in nums if x != max1]
    if not filtered:
        return None
    return max(filtered)
def max_product_subarray(nums):
    if not nums:
        return 0
    max_so_far = min_so_far = result = nums[0]
    for num in nums[1:]:
        current_num = num
        candidates = [current_num, max_so_far * current_num, min_so_far * current_num]
        new_max = max(candidates)
        new_min = min(candidates)
        max_so_far, min_so_far = new_max, new_min
        if new_max > result:
            result = new_max
    return result
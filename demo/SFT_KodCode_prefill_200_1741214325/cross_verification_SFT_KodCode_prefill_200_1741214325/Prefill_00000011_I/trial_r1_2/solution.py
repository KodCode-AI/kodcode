def max_product_subarray(nums):
    if not nums:
        return 0
    global_max = current_max = current_min = nums[0]
    for num in nums[1:]:
        temp_max = max(num, current_max * num, current_min * num)
        temp_min = min(num, current_max * num, current_min * num)
        current_max, current_min = temp_max, temp_min
        if current_max > global_max:
            global_max = current_max
    return global_max
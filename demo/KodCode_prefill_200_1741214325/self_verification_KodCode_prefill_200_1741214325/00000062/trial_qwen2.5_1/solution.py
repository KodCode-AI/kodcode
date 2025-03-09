def find_second_maximum(nums):
    """
    Returns the second maximum number in a list of integers. Returns None if there is no such number.
    """
    if len(nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in nums:
        if num > max_num:
            second_max_num, max_num = max_num, num
        elif max_num > num > second_max_num:
            second_max_num = num
    return second_max_num if second_max_num != max_num else None
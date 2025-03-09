def second_smallest(nums):
    """
    Returns the second smallest unique number in the list `nums`.
    Returns None if there are less than two unique numbers.
    """
    unique_nums = set(nums)
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[1]
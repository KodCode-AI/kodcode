def single_number(nums):
    """
    Returns the single number in a list where every other number appears exactly twice.
    """
    single = 0
    for num in nums:
        single ^= num
    return single
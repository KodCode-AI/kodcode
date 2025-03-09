def single_number(nums):
    """
    Find the single number in a list where every other number appears exactly twice.
    Assumes one and only one number appears once and all others appear twice.
    Returns the number that appears exactly once.

    Args:
    nums (List[int]): A list of integers.

    Returns:
    int: The integer that appears exactly once.
    """
    unique = 0
    for num in nums:
        unique ^= num
    return unique
def find_next_power_of_two(number: int) -> int:
    """
    Returns the smallest power of two greater than the given non-negative integer.
    If the input is 0, it returns 1.
    """
    # Edge case: if the number is 0, return 1
    if number == 0:
        return 1
    
    power = 1
    while power < number:
        power *= 2
    return power
def find_next_power_of_two(number: int) -> int:
    """
    Returns the smallest power of two greater than the given non-negative integer.
    If the input is 0, returns 1.
    >>> find_next_power_of_two(0) == 1
    >>> find_next_power_of_two(1) == 2
    >>> find_next_power_of_two(15) == 16
    >>> find_next_power_of_two(16) == 32
    """
    if number == 0:
        return 1
    return 1 << number.bit_length()
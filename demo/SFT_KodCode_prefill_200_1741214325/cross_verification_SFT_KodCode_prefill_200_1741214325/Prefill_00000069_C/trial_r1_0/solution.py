def count_trailing_zeros(number: int) -> int:
    """
    Counts and returns the number of trailing zeros in the given integer.
    """
    if number == 0:
        return 1  # Special case where the number itself is 0
    count = 0
    while number % 10 == 0:
        count += 1
        number //= 10
    return count
def count_trailing_zeros(number: int) -> int:
    """
    Counts the number of trailing 0 bits in the binary representation of a given integer.
    """
    count = 0
    while number and number % 2 == 0:
        number >>= 1
        count += 1
    return count
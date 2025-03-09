def is_power_of_two(n: int) -> bool:
    """
    Checks if the given number n is a power of two.
    """
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
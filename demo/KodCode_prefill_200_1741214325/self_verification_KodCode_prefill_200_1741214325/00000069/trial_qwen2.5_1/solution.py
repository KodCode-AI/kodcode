def count_trailing_zeros(n):
    """
    Returns the count of trailing zeros in the given number n.
    """
    count = 0
    while n % 10 == 0 and n != 0:
        count += 1
        n //= 10
    return count
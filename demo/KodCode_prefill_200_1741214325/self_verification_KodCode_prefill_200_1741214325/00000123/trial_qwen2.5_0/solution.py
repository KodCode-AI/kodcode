def is_prime(n):
    """
    Returns True if n is a prime number, else returns False.
    
    A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
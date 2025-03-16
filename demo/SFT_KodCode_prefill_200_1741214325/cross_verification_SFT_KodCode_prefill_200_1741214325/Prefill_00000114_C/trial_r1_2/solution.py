import math

def is_prime(n: int) -> bool:
    """Determines if a given number n is a prime number.
    Returns True if n is a prime, False otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
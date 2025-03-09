def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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

def find_next_prime(value: int) -> int:
    """Find the next prime number greater than the given value."""
    next_number = value + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number
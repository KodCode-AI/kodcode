def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """
    Returns a list of all prime numbers within the given range [start, end] inclusive.
    """
    return [n for n in range(start, end + 1) if is_prime(n)]
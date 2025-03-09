def is_prime(n):
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

def find_primes_in_range(start, end):
    """
    Returns a list of all prime numbers between start and end inclusive.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
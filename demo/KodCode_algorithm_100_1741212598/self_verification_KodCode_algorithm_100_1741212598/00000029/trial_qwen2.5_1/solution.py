from math import isqrt

def is_prime(n: int) -> bool:
    """
    Returns True if n is a prime number, else False.
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

def check_primes_with_property(limit: int) -> int:
    count = 0
    for p in range(2, limit):
        if is_prime(p):
            n = 1
            while True:
                value = (n**3 + n**2 * p)
                if is_cube(value):
                    count += 1
                    break
                n += 1
    return count

def is_cube(n: int) -> bool:
    """
    Returns True if n is a perfect cube, else False.
    """
    cube_root = round(n ** (1/3))
    return cube_root ** 3 == n
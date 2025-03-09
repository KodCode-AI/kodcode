from sympy import isprime

def check_primes_with_property(limit: int) -> int:
    """
    Counts the number of prime numbers below the given limit that satisfy the property
    that there exists a positive integer n such that n^3 + n^2 * p is a perfect cube.
    """
    def finds_property(p):
        for n in range(1, int(limit**0.25) + 1):
            if (n**3 + n**2 * p) ** (1/3) == int((n**3 + n**2 * p) ** (1/3)):
                return True
        return False

    count = 0
    for p in range(2, limit):
        if isprime(p) and finds_property(p):
            count += 1
    return count
def extended_gcd(a, b):
    """
    Returns a tuple (gcd, x, y) such that gcd is the greatest common divisor of a and b,
    and x, y are the coefficients satisfying Bezout's identity ax + by = gcd(a, b).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

def calculate_k(m: int, n: int) -> int:
    """
    Calculates k = a^2 + b^2 where a and b are the Bezout coefficients for integers m and n.
    """
    gcd, a, b = extended_gcd(m, n)
    k = a**2 + b**2
    return k
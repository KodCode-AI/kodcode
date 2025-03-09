def extended_gcd(a, b):
    """
    Returns the coefficients x and y such that ax + by = gcd(a, b),
    along with the greatest common divisor of a and b.
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def calculate_k(m: int, n: int) -> int:
    """
    Returns k = a^2 + b^2 where a and b are integers such that am + bn = gcd(m, n).
    """
    gcd, a, b = extended_gcd(m, n)
    k = a**2 + b**2
    return k
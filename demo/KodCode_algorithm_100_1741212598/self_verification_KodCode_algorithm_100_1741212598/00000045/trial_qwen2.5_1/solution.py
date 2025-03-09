def gcd_by_iterative(a, b):
    """
    Returns the greatest common divisor of a and b using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b,
    and x, y are the coefficients such that gcd = ax + by.
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def find_mod_inverse(a, m):
    """
    Returns the modular inverse of a modulo m if it exists.
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"mod inverse of {a} and {m} does not exist")
    else:
        return x % m
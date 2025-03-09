def gcd_by_iterative(a, b):
    """
    Returns the greatest common divisor of a and b using the iterative version of the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def find_mod_inverse(a, m):
    """
    Returns the modular inverse of a modulo m using the Extended Euclidean Algorithm.
    
    Raises ValueError if the modular inverse does not exist.
    """
    if gcd_by_iterative(a, m) != 1:
        raise ValueError(f"mod inverse of {a} and {m} does not exist")
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    
    return u1 % m
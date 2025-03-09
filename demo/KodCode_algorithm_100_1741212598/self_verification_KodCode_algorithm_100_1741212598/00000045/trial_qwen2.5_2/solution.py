def gcd_by_iterative(a, b):
    """
    Returns the greatest common divisor of a and b using an iterative approach.
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
    
    m0, x0, x1 = m, 0, 1
    while a > 1:
        # q is quotient
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    
    # Make x1 positive
    if x1 < 0:
        x1 += m0
    
    return x1
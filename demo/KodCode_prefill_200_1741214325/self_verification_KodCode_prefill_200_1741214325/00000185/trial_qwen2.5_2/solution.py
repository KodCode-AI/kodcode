def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Returns the least common multiple of a and b.
    """
    return a * b // gcd(a, b)

def smallest_multiple(a, b):
    """
    Returns the smallest number that is a multiple of both a and b.
    """
    return lcm(a, b)
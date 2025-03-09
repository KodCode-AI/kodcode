def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a
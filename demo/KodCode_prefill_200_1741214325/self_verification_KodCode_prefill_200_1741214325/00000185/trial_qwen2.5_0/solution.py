def gcd(a, b):
    """
    Returns the greatest common divisor (GCD) of a and b using Euclid's algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Returns the least common multiple (LCM) of a and b using the formula lcm(a, b) = abs(a*b) // gcd(a, b).
    """
    return abs(a * b) // gcd(a, b)
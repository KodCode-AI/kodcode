def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Returns the least common multiple (LCM) of two numbers.
    """
    return abs(a * b) // gcd(a, b)
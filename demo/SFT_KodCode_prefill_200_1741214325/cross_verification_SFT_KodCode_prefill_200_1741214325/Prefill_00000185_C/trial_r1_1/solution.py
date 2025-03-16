def gcd(a: int, b: int) -> int:
    """ Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm(a: int, b: int) -> int:
    """ Returns the least common multiple (LCM) of two numbers."""
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)
def gcd(a: int, b: int) -> int:
    """ Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm."""
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    """ Returns the least common multiple (LCM) of two numbers."""
    a_abs = abs(a)
    b_abs = abs(b)
    if a_abs == 0 and b_abs == 0:
        return 0  # or raise an error, as LCM(0,0) is undefined
    g = gcd(a_abs, b_abs)
    return (a_abs * b_abs) // g
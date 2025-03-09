from typing import List, Tuple

def diophantine_all_values(a: int, b: int, c: int, upper_limit: int) -> List[Tuple[int, int]]:
    """
    Find all pairs (x, y) that satisfy the Diophantine equation ax + by = c
    within the range -upper_limit <= x, y <= upper_limit.
    """
    # First, find one particular solution using the extended Euclidean algorithm
    x0, y0, _ = extended_gcd(a, b)
    if c % gcd(a, b) != 0:
        return []  # No solutions exist

    # Scale the solution to the constant c
    x0 *= c // gcd(a, b)
    y0 *= c // gcd(a, b)

    # Find the formula for the general solution
    x0, y0 = x0 // b, y0 // a

    # Generate all solutions within the specified range
    solutions = []
    for k in range((-upper_limit - x0) // -b + 1):
        x = x0 + b * k
        y = y0 - a * k
        if -upper_limit <= x <= upper_limit and -upper_limit <= y <= upper_limit:
            solutions.append((x, y))
        if -upper_limit <= x0 + b * (k + 1) <= upper_limit:
            break
    return solutions

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm that returns the gcd of a and b,
    and the coefficients of Bézout's identity.
    """
    s, t, s_old, t_old = 0, 1, 1, 0
    r, r_old = b, a

    while r != 0:
        quotient = r_old // r
        r_old, r = r, r_old - quotient * r
        s_old, s = s, s_old - quotient * s
        t_old, t = t, t_old - quotient * t

    return a if a != 0 else b, s_old, t_old

def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a
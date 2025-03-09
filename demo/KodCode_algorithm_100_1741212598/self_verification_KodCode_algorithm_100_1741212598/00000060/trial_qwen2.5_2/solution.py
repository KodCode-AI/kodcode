from typing import List, Tuple

def diophantine_all_values(a: int, b: int, c: int, upper_limit: int) -> List[Tuple[int, int]]:
    """
    Finds all pairs (x, y) of integers that satisfy the equation a*x + b*y = c
    within the range -upper_limit <= x, y <= upper_limit.
    """
    # Check if the equation has solutions
    if c % gcd(a, b) != 0:
        return []

    # Find one particular solution using the extended Euclidean algorithm
    x0, y0 = extended_euclidean_algorithm(a, b, c)

    # Ensure the solution is within the range
    x0, y0 = ensure_in_range(x0, y0, a, b, upper_limit)

    # Generate all solutions within the specified range
    solutions = []
    for k in range(-upper_limit, upper_limit + 1):
        x = x0 + k * (b // gcd(a, b))
        y = y0 - k * (a // gcd(a, b))
        if -upper_limit <= x <= upper_limit and -upper_limit <= y <= upper_limit:
            solutions.append((x, y))
    
    return solutions

def extended_euclidean_algorithm(a: int, b: int, c: int) -> Tuple[int, int]:
    """
    Finds one particular solution (x0, y0) to the equation ax + by = c.
    """
    x0, y0, gcd_value = extended_gcd(a, b)
    if c % gcd_value != 0:
        return (0, 0)  # No solution if c is not divisible by gcd(a, b)
    x0 *= c // gcd_value
    y0 *= c // gcd_value
    return (x0, y0)

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm to find x and y such that ax + by = gcd(a, b).
    """
    if a == 0:
        return (0, 1, b)
    else:
        x1, y1, gcd_value = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (x, y, gcd_value)

def ensure_in_range(x: int, y: int, a: int, b: int, upper_limit: int) -> Tuple[int, int]:
    """
    Adjust the initial solution to ensure it is within the given range if necessary.
    """
    # Calculate the range adjustment needed for x and y
    x_adjust = (upper_limit - x) // (b // gcd(a, b))
    if x + x_adjust * (b // gcd(a, b)) > upper_limit:
        x_adjust -= 1
    x_new = x + x_adjust * (b // gcd(a, b))
    y_new = y - x_adjust * (a // gcd(a, b))
    return (x_new, y_new)
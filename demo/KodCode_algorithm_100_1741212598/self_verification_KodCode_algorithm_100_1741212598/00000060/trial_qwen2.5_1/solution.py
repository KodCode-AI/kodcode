from typing import List, Tuple

def diophantine_all_values(a: int, b: int, c: int, upper_limit: int) -> List[Tuple[int, int]]:
    """
    Find all integer pairs (x, y) that satisfy the equation a*x + b*y = c within the given range [-upper_limit, upper_limit].
    """
    # First, use the extended Euclidean algorithm to find one particular solution (x0, y0)
    def extended_gcd(aa, bb):
        lastremainder, remainder = abs(aa), abs(bb)
        x, lastx, y, lasty = 0, 1, 1, 0
        while remainder:
            lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
            x, lastx = lastx - quotient*x, x
            y, lasty = lasty - quotient*y, y
        return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
    
    _, x0, y0 = extended_gcd(a, b)
    if c % lastremainder != 0:
        return []  # No solution exists
    
    # Scale the solution by c / lastremainder
    x0 *= c // lastremainder
    y0 *= c // lastremainder
    
    # Find the general solution
    solutions = []
    hcf = lastremainder
    steps_x = b // hcf
    steps_y = a // hcf
    
    # Generate solutions within the given range
    for k in range((-upper_limit - x0) // steps_x + 1):
        x = x0 + k * steps_x
        if -upper_limit <= x <= upper_limit:
            y = y0 - k * steps_y
            if -upper_limit <= y <= upper_limit:
                solutions.append((x, y))
    
    return solutions
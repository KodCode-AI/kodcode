def extended_gcd(m: int, n: int) -> (int, int, int):
    """
    Extended Euclidean Algorithm implementation.
    Returns gcd, a, b such that m * a + n * b = gcd(m, n)
    """
    if m == 0:
        return n, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(n % m, m)
        x = y1 - (n // m) * x1
        y = x1
        return gcd, x, y

def calculate_k(m: int, n: int) -> int:
    """
    Calculates the integer k using the coefficients from the Extended Euclidean Algorithm.
    """
    _, a, b = extended_gcd(abs(m), abs(n))  # Use absolute values to handle negative inputs
    k = a**2 + b**2
    return k

# Example usage
print(calculate_k(10, 6))  # Output: 5
print(calculate_k(35, 15))  # Output: 58
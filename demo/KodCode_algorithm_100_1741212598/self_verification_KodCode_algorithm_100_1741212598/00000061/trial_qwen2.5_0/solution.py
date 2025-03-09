def find_pythagorean_triplet_product(N: int) -> int:
    """
    Finds the product of the Pythagorean triplet (a, b, c) such that:
    - a + b + c = N
    - a^2 + b^2 = c^2
    Returns the product a * b * c.
    """
    for a in range(1, N // 3 + 1):
        for b in range(a + 1, (N - a) // 2 + 1):
            c = N - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return -1  # Return -1 if no triplet is found, though we expect a solution within constraints
def find_pythagorean_triplet_product(N: int) -> int:
    """
    Finds the product of the Pythagorean triplet (a, b, c) for which a + b + c = N.
    """
    for a in range(1, N // 3):
        for b in range(a + 1, N // 2):
            c = N - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return -1  # In case no triplet is found, though there should be one for valid N
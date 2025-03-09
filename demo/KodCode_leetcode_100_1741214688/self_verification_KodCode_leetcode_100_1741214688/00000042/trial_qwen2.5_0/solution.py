def add_binary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return the sum of a and b as a binary string.
    """
    return bin(int(a, 2) + int(b, 2))[2:]
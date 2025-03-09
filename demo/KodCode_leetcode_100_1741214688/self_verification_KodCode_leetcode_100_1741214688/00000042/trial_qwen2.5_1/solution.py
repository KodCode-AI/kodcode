def add_binary(a: str, b: str) -> str:
    """
    Given two binary strings, return their sum as a binary string.
    """
    # Convert binary strings to integers, sum them, then convert back to binary
    return bin(int(a, 2) + int(b, 2))[2:]
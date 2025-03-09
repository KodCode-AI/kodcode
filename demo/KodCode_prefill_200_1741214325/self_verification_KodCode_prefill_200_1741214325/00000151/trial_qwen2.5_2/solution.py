def decimal_to_binary(n: int) -> str:
    """
    Converts a decimal number to its binary representation without using Python's built-in bin() function.
    """
    if n == 0:
        return "0"
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2
    binary.reverse()
    return ''.join(binary)
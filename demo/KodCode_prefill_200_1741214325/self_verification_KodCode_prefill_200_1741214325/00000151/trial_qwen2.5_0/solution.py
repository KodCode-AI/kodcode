def decimal_to_binary(n: int) -> str:
    """
    Converts a decimal number to its binary representation without using the built-in bin function.
    
    Parameters:
    n (int): The decimal number to be converted.
    
    Returns:
    str: The binary representation of the decimal number.
    """
    if n == 0:
        return "0"
    binary_str = ""
    while n > 0:
        remainder = n % 2  # Find the remainder when n is divided by 2
        binary_str = str(remainder) + binary_str  # Prepend the remainder to the binary string
        n = n // 2  # Divide n by 2 and take the floor
    return binary_str
def is_binary_palindrome(number: int) -> bool:
    """
    Checks if the binary representation of the given number is a palindrome.
    """
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    binary_str = bin(number)[2:]  # Convert to binary and remove the '0b' prefix
    return binary_str == binary_str[::-1]
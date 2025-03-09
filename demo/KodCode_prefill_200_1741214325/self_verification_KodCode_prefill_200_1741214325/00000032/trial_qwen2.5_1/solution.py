def is_binary_palindrome(n: int) -> bool:
    """
    Checks if the binary representation of a number is a palindrome.

    :param n: Integer to check
    :return: True if binary representation is a palindrome, False otherwise
    """
    binary_str = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    return binary_str == binary_str[::-1]
def is_binary_palindrome(number):
    """
    Returns True if the binary representation of the number is a palindrome, otherwise False.
    """
    binary_str = bin(number)[2:]  # Convert number to binary and remove the '0b' prefix.
    return binary_str == binary_str[::-1]
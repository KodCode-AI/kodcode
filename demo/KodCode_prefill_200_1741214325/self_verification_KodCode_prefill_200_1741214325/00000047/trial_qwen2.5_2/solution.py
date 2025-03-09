def is_palindrome(s: str) -> bool:
    """
    Returns True if the given string is a palindrome, False otherwise.
    """
    return s == s[::-1]
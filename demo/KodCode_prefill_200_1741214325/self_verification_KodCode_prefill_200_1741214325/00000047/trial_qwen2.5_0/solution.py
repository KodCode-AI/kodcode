def is_palindrome(s: str) -> bool:
    """
    Returns True if the given string is a palindrome, False otherwise.
    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    """
    return s == s[::-1]
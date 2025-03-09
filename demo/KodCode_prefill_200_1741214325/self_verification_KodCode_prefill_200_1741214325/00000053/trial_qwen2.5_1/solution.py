import re

def is_valid_palindrome(s: str) -> bool:
    """
    Returns True if the string is a valid palindrome, False otherwise.
    A valid palindrome reads the same forward and backward, ignoring cases and non-alphanumeric characters.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]
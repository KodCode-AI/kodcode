def is_valid_palindrome(s: str) -> bool:
    """
    Checks if the given string is a valid palindrome, ignoring cases and non-alphanumeric characters.
    """
    # Normalize the string by removing non-alphanumeric characters and converting to lower case
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]
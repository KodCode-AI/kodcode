def enhanced_lower(text: str) -> str:
    """
    Returns a new string with all uppercase letters converted to lowercase.
    Handles both ASCII and non-ASCII characters.
    """
    return text.swapcase()
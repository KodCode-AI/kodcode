def modify_string(s):
    """
    Converts the first and last characters of the string to uppercase.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: The modified string with the first and last characters in uppercase.
    """
    if len(s) <= 1:
        return s.upper()
    else:
        return s[0].upper() + s[1:-1] + s[-1].upper()
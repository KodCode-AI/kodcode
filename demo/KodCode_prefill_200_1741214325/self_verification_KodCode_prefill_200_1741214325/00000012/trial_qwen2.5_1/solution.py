def capitalize_first_last_char(s):
    """
    Converts the first and last characters of the string to uppercase and returns the modified string.
    If the string has less than 2 characters, it returns the string as is.
    """
    if len(s) < 2:
        return s
    return s[0].upper() + s[1:-1] + s[-1].upper()
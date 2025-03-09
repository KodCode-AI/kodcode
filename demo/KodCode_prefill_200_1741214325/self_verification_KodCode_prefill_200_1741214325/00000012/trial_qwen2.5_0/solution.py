def convert_chars_to_uppercase(s):
    """
    Converts the first and last characters of a string to uppercase and returns the modified string.
    If the string is empty or has only one character, it returns the string as is but in uppercase.
    """
    if len(s) == 0:
        return s
    elif len(s) == 1:
        return s.upper()
    else:
        return s[0].upper() + s[1:-1] + s[-1].upper()
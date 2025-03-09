def count_uppercase(s):
    """
    Returns the number of uppercase letters in the string `s`.
    """
    return sum(1 for c in s if c.isupper())
def count_uppercase_letters(s):
    """
    Counts and returns the number of uppercase letters in the given string.
    """
    return sum(1 for c in s if c.isupper())
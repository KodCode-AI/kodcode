def count_chars(string):
    """
    Counts the number of unique characters, digits, and special characters
    in a given string and returns the counts as a tuple (unique_chars, digits, special_chars).
    """
    unique_chars = set(string)
    digits = sum(c.isdigit() for c in string)
    special_chars = sum(not c.isalnum() for c in string)
    return (len(unique_chars), digits, special_chars)
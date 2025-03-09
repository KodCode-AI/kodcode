def count_chars_digits_special(s):
    """
    Counts and returns the number of unique characters, digits, and special characters in a given string.
    Returns a tuple in the form (unique_chars, digits, special_chars).
    """
    char_set = set(s)
    unique_chars = len(char_set)
    
    digits = sum(c.isdigit() for c in s)
    special_chars = sum(not c.isalnum() and not c.isspace() for c in s)
    
    return (unique_chars, digits, special_chars)
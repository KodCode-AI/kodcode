def char_counter(input_string):
    """
    Given an input string, returns a tuple containing the count of unique characters,
    digits, and special characters.
    """
    unique_chars = set(input_string)
    unique_chars_count = len(unique_chars)
    digits = sum(c.isdigit() for c in input_string)
    special_chars = len(input_string) - unique_chars_count - digits
    return (unique_chars_count, digits, special_chars)
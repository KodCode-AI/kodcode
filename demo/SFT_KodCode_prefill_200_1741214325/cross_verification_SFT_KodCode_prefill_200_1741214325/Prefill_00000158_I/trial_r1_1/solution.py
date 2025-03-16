def char_count(input_string, char):
    """
    Count the number of times a specific character appears in a string.

    Args:
        input_string (str): The string to search in.
        char (str): The character to count. Must be a single character.

    Returns:
        int: The number of times 'char' appears in 'input_string'.
    """
    if len(char) != 1:
        return 0
    return input_string.count(char)
def string_to_ascii_list(input_string):
    """
    Converts a given string to a list of integers, where each integer is the ASCII value of each character in the string.
    """
    return [ord(char) for char in input_string]
def string_to_ascii_list(input_string):
    """
    Converts the given string into a list of ASCII values of each character.
    
    :param input_string: String to be converted
    :return: List of ASCII values
    """
    return [ord(char) for char in input_string]
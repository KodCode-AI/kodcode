import re

def is_valid_identifier(name):
    """
    Returns True if the given string is a valid Python identifier, otherwise False.
    A valid Python identifier starts with a letter (a-z, A-Z) or an underscore (_),
    followed by zero or more letters, digits (0-9), or underscores.
    """
    pattern = r'^[a-zA-Z_][a-zA-Z_0-9]*$'
    return bool(re.match(pattern, name))
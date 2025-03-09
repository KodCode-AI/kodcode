import re

def is_valid_double(s):
    """
    Returns True if the given string is a valid double, False otherwise.
    """
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    return bool(re.match(pattern, s))
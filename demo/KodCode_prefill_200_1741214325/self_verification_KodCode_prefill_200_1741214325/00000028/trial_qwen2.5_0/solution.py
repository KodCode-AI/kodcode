import re

def is_valid_double(s):
    """
    Returns True if the input string is a valid double, otherwise False.
    """
    # Regular expression for matching valid doubles
    double_pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(double_pattern, s))
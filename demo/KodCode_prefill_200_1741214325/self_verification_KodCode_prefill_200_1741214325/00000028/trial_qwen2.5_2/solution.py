import re

def is_valid_double(s):
    """
    Returns True if the string is a valid double, False otherwise.
    A valid double is defined as a number with a decimal point.
    """
    # Regular expression to match a valid double
    double_pattern = re.compile(r'^-?\d+(?:\.\d+)?$')
    return bool(double_pattern.match(s))
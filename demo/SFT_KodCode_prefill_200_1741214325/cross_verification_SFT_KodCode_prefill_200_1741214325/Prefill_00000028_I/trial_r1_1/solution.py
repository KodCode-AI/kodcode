import re

def is_valid_double(s):
    pattern = r'^[+-]?(\d+\.\d*|\.\d+)([eE][+-]?\d+)?$'
    return re.match(pattern, s) is not None
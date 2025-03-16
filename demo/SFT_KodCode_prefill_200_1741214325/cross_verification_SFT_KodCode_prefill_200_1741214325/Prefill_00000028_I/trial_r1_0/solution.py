import re

def is_valid_double(s):
    pattern = r'^[+-]?(\d+\.?\d*|\.\d+)$'
    return bool(re.fullmatch(pattern, s))
import re

def str_to_int(s):
    stripped = s.strip()
    if not stripped:
        return None
    if not re.match(r'^-?\d+$', stripped):
        return None
    return int(stripped)
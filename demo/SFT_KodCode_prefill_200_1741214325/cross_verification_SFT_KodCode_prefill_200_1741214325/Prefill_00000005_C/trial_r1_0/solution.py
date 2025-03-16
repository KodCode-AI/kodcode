import re

def str_to_int(s: str) -> int:
    match = re.search(r'\s*([+-]?\d+)', s)
    if match:
        return int(match.group(1))
    else:
        return 0
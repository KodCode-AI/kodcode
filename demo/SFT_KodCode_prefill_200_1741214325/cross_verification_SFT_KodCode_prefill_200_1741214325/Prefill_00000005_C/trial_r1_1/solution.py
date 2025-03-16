import re

def str_to_int(s: str) -> int:
    stripped = s.strip()
    match = re.search(r'([+-]?\d+)', stripped)
    return int(match.group()) if match else 0
def str_to_int(s):
    stripped = s.strip()
    if not stripped:
        return None
    if stripped[0] == '-':
        if len(stripped) == 1:
            return None
        if not stripped[1:].isdigit():
            return None
    else:
        if not stripped.isdigit():
            return None
    return int(stripped)
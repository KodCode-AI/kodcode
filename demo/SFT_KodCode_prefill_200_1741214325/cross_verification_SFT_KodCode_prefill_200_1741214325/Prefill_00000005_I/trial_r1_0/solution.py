def str_to_int(s):
    s = s.strip()
    if not s:
        return None
    sign = 1
    start = 0
    if s[0] == '+':
        start = 1
    elif s[0] == '-':
        sign = -1
        start = 1
    num_part = s[start:]
    if not num_part.isdigit():
        return None
    return sign * int(num_part)
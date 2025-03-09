def string_to_int(s: str) -> int:
    """
    Converts a string to an integer, handling leading/trailing whitespaces and invalid characters.
    Returns 0 for empty strings or strings with no valid digits.
    """
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    start = 0
    if s[0] in ('-', '+'):
        if s[0] == '-':
            sign = -1
        start = 1
    
    integer_value = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break
        integer_value = integer_value * 10 + int(s[i])
    
    if sign == -1:
        integer_value *= -1
    
    return max(min(integer_value, 2**31 - 1), -2**31)
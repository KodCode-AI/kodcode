def str_to_int(s: str) -> int:
    """
    Converts a string to an integer, handling leading/trailing whitespaces and invalid characters.
    """
    s = s.strip()  # Remove leading and trailing whitespaces
    if not s:  # Empty string after stripping
        return 0
    
    sign = 1
    i = 0
    if s[0] == '-':  # Negative number
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1
    
    num = 0
    for c in s[i:]:
        if not '0' <= c <= '9':
            break
        num = num * 10 + (ord(c) - ord('0'))
    
    return max(-2**31, min(num * sign, 2**31 - 1))
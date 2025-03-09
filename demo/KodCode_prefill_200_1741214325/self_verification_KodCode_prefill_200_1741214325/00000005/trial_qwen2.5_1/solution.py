import string

def str_to_int(s: str) -> int:
    """
    Converts a string to an integer, considering edge cases with leading/trailing whitespaces and invalid characters.
    """
    # Remove leading and trailing whitespaces
    s = s.strip()
    
    if not s:
        return 0
    
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1

    int_val = 0
    for char in s[i:]:
        if char.isdigit():
            int_val = int_val * 10 + int(char)
        else:
            break
    
    # Handle 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if sign * int_val > INT_MAX:
        return INT_MAX
    elif sign * int_val < INT_MIN:
        return INT_MIN
    else:
        return sign * int_val
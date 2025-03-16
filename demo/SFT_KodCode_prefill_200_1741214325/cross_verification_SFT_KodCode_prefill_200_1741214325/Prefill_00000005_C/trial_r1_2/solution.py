def str_to_int(s: str) -> int:
    s_clean = s.strip()
    if not s_clean:
        return 0
    
    sign = 1
    i = 0
    
    if i < len(s_clean) and s_clean[i] in '+-':
        sign = -1 if s_clean[i] == '-' else 1
        i += 1
    
    digits = []
    while i < len(s_clean) and s_clean[i].isdigit():
        digits.append(s_clean[i])
        i += 1
    
    if not digits:
        return 0
    
    number = int(''.join(digits)) * sign
    return number
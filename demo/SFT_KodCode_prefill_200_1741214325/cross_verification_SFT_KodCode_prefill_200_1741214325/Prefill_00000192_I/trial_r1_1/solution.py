def first_repeating_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return -1
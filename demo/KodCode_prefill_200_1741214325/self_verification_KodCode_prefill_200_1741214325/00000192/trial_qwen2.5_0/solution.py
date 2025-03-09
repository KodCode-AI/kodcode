def first_repeating_char(s):
    """
    Finds and returns the first repeating character in the given string.
    If no character repeats, returns -1.
    """
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return -1
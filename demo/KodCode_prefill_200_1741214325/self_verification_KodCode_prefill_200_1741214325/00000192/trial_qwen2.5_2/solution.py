def first_repeating_char(s: str) -> int:
    """
    Finds the first repeating character in the string `s`.
    If no character is repeating, returns -1.
    """
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return -1
def first_repeating_char(s: str) -> int:
    """
    Finds the first repeating character in the string `s` and returns its index.
    If no character is repeating, returns -1.
    """
    seen = set()
    for i, char in enumerate(s):
        if char in seen:
            return i
        seen.add(char)
    return -1
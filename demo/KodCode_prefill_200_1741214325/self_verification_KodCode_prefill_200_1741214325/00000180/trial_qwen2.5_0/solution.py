def has_separated_repeats(s: str) -> bool:
    """
    Returns True if the string s contains at least one sequence of 
    consecutive repeating characters that are not adjacent to each other;
    otherwise, returns False.

    >>> has_separated_repeats("abcddcba")
    False
    >>> has_separated_repeats("a")
    False
    >>> has_separated_repeats("abdccbda")
    True
    """
    prev_char = None
    repeat_count = 0
    for i, char in enumerate(s):
        if char == prev_char:
            repeat_count += 1
            # Check if the repeat is not adjacent
            if i > 0 and s[i-1] != char:
                return True
        else:
            prev_char = char
            repeat_count = 1

    return False
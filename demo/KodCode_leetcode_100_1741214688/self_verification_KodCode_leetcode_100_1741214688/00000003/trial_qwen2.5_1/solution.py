def smallest_string(s: str) -> str:
    """
    Returns the lexicographically smallest string possible by swapping adjacent
    characters if the first character has a higher ASCII value than the second.
    """
    s_list = list(s)
    i = 0
    while i < len(s_list) - 1:
        if s_list[i] > s_list[i + 1]:
            s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
            i = 0
        else:
            i += 1
    return ''.join(s_list)
def first_repeating_char(s: str) -> str:
    first_occurrence = {}
    for i, c in enumerate(s):
        if c not in first_occurrence:
            first_occurrence[c] = i
    for i, c in enumerate(s):
        if i > first_occurrence[c]:
            return c
    return -1
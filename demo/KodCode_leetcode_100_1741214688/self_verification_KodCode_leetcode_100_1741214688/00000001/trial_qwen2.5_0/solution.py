def largest_string(s: str, k: int) -> str:
    """
    Returns the lexicographically largest string that can be obtained by performing
    the specified operations on s, k times.
    """
    n = len(s)
    if k == 0 or n == 0:
        return s

    # If k is greater than or equal to half the length of the string, we can sort
    # the entire string in descending order to get the maximum lexicographic string
    if k >= (n + 1) // 2:
        return ''.join(sorted(s, reverse=True))

    # Otherwise, we need to simulate the operations
    for _ in range(k):
        max_slice = ""
        max_char = s[0]
        for i in range(1, n):
            if s[i] >= max_char:
                max_char = s[i]
                max_slice = s[i:]
                break
        if max_slice:
            s = max_slice + s[s.index(max_slice) + len(max_slice):]
        else:
            break

    return s
def countGoodSubstrings(s: str) -> int:
    """
    Counts the number of good substrings in the binary string s.
    A good substring does not contain any leading zeros and has an even length.
    """
    count = 0
    n = len(s)
    for i in range(n - 1):
        if s[i] == '0':
            continue
        if i + 1 < n and s[i + 1] == '0':
            continue
        if (i + 2 < n) and s[i + 2] == '1' and s[i + 3] == '1':
            count += 1
            i += 3
    return count
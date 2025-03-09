def smallest_string(s):
    """
    Returns the lexicographically smallest string that can be obtained.
    """
    result = ""
    i = 0
    n = len(s)
    while i < n:
        start = i
        while i < n and s[i] == s[start]:
            i += 1
        if i - start > 1:
            result += s[start]
        else:
            result += s[start:i]
    return result.replace(s[0], 'a')
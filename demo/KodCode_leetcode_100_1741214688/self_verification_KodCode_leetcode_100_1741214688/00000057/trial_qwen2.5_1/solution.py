def smallest_by_reversing_substrings(s, k):
    """
    Returns the lexicographically smallest string that can be obtained
    by reversing any number of substrings of length k in the input string s.
    """
    n = len(s)
    result = list(s)
    for i in range(0, n - k + 1):
        substring = s[i:i+k]
        min_sub = min(s[i:i+k], s[i:i+k][::-1])
        if min_sub == substring[::-1]:
            result[i:i+k] = s[i:i+k][::-1]
        else:
            result[i:i+k] = s[i:i+k]
    return ''.join(result)
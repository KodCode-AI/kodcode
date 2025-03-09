def form_smallest_palindrome(s: str) -> str:
    """
    Returns the lexicographically smallest palindrome by swapping at most one pair of adjacent characters.
    If it's not possible, returns the original string.
    """
    s_list = list(s)
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            for j in range(i + 1, n - i):
                if s[j] == s[n - 1 - i]:
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    return ''.join(s_list)
            return s
    return ''.join(s_list)
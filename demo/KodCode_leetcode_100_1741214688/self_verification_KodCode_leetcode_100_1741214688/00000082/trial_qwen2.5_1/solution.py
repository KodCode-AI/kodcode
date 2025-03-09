def min LexicoPalindrome(s: str, k: int) -> str:
    """
    Returns the lexicographically smallest palindrome that can be obtained by swapping adjacent characters at most k times.
    If it's not possible to form a palindrome, returns an empty string.
    """
    if k >= len(s) // 2:
        return s == s[::-1] and s or ""

    def reverse_substring(s, start, end):
        while start < end:
            s = s[:start] + s[end] + s[start+1:end] + s[start] + s[end+1:]
            start += 1
            end -= 1
        return s

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if k < 2:
                return ""
            k -= 1
            s = reverse_substring(s, i, n - i - 1)

    return s
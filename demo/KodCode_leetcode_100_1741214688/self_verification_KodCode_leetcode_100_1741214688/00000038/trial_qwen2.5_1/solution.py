def longest_alphabetic_substring(s: str) -> int:
    """
    Given a string s, return the length of the longest substring that can be obtained
    by replacing at most one character in s with any other character, such that
    the resulting substring is an alphabetical continuous string.
    """
    max_len = 1
    start = 0
    replace_char = float('-inf')
    for end in range(1, len(s)):
        if ord(s[end]) != ord(s[end - 1]) + 1:
            if s[end] != s[end - 1]:
                prev_char = s[end - 1]
                replace_char = max(replace_char, s[end - 1])
            start = max(start, end - 1 if s[end] != s[end - 1] else replace_char + 1)
            replace_char = s[end - 1]
        max_len = max(max_len, end - start + 1)
    return max_len
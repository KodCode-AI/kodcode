def longest_substring_without_repeating(s: str) -> str:
    """
    Finds the longest substring without repeating characters in a given string.
    """
    if not s:
        return ""

    start = 0
    max_length = 0
    max_substring = ""
    used_chars = {}

    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            if (i - start + 1) > max_length:
                max_length = i - start + 1
                max_substring = s[start:i+1]

        used_chars[char] = i

    return max_substring
def longest_substring_with_all_chars(s: str) -> str:
    """
    Returns the longest substring of s that contains at least one occurrence of every character in s.
    If there are multiple such substrings of the same length, the earliest one is returned.
    If no such substring exists, returns an empty string.
    """
    if not s:
        return ""

    char_to_last_index = {}
    start = 0
    min_start = 0
    max_length = 0

    for end in range(len(s)):
        char = s[end]
        if char in char_to_last_index:
            start = max(start, char_to_last_index[char] + 1)
        char_to_last_index[char] = end

        if end - start + 1 > max_length:
            max_length = end - start + 1
            min_start = start

    return s[min_start:min_start + max_length] if max_length > 0 else ""
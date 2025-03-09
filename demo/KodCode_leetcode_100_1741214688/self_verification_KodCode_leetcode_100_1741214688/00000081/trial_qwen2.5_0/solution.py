def longest_substring_with_all_chars(s):
    """
    Returns the longest substring that contains at least one occurrence of every character in the string `s`.
    If there are multiple substrings of the same length, returns the earliest one.
    If no such substring exists, returns an empty string.
    """
    if not s:
        return ""

    char_last_position = {}
    start = 0
    max_length = 0
    result = ""

    for end, char in enumerate(s):
        if char in char_last_position:
            start = max(start, char_last_position[char] + 1)
        char_last_position[char] = end

        if end - start + 1 > max_length:
            max_length = end - start + 1
            result = s[start:end + 1]

    return result
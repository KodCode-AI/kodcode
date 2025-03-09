def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    char_index_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
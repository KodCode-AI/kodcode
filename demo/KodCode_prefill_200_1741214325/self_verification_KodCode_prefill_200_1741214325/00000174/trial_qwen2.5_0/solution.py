def longest_substring_two_distinct(s: str) -> int:
    """
    Returns the length of the longest substring of s that contains at most two distinct characters.
    """
    if not s:
        return 0

    n = len(s)
    max_length = 1
    start, end = 0, 0
    char_map = {}

    while end < n:
        if len(char_map) < 3:
            char_map[s[end]] = char_map.get(s[end], 0) + 1
            end += 1

        if len(char_map) == 3:
            max_length = max(max_length, end - start)
            # Remove the earliest character to maintain at most 2 distinct characters
            start_char = min(char_map, key=char_map.get)
            char_map.pop(start_char)
            start += char_map[start_char]
            char_map[s[end - 1]] = 1

        max_length = max(max_length, end - start)

    return max_length
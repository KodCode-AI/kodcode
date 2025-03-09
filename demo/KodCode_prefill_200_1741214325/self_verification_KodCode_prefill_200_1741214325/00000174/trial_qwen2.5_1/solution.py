def longest_substring_with_two_distinct_chars(s: str) -> int:
    """
    Finds the longest substring of the given string `s` that contains at most two distinct characters.
    """
    if not s:
        return 0

    max_length = 1
    start = 0
    char_map = {}
    max_length_char = s[0]

    for end in range(len(s)):
        char_map[s[end]] = char_map.get(s[end], 0) + 1

        while len(char_map) > 2:
            char_map[s[start]] -= 1
            if char_map[s[start]] == 0:
                del char_map[s[start]]
            start += 1

        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_length_char = s[start:end+1]

    return max_length
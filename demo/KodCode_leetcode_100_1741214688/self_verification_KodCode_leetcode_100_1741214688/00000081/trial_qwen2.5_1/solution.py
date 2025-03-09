def longest_substring_with_all_chars(s: str) -> str:
    """
    Finds the longest substring that contains at least one occurrence of every character in the string.
    If there are multiple substrings of the same length, returns the one that appears earliest.
    If no such substring exists, returns an empty string.
    """
    n = len(s)
    if n == 0:
        return ""
    
    char_positions = {ch: [] for ch in set(s)}
    
    for i, ch in enumerate(s):
        char_positions[ch].append(i)
    
    start, end = 0, 0
    max_len = 0
    min_end = float('inf')
    char_count = len(char_positions)
    
    while end < n:
        if char_count == 0:
            if end - start + 1 > max_len:
                max_len = end - start + 1
                min_end = start
            start = char_positions[s[start]].pop(0)
            if not char_positions[s[start]]:
                del char_positions[s[start]]
            char_count += 1
            start += 1
        else:
            char_count -= 1
            end += 1
            if end < n:
                char_count += 1
                if s[end] in char_positions:
                    char_positions[s[end]].append(end)
    
    return s[min_end:min_end + max_len] if max_len > 0 else ""
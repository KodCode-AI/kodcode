def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring that contains at most two distinct characters.
    """
    if not s:
        return 0
    
    left, max_len = 0, 0
    char_map = {}
    
    for right in range(len(s)):
        char = s[right]
        char_map[char] = char_map.get(char, 0) + 1
        
        while len(char_map) > 2:
            left_char = s[left]
            char_map[left_char] -= 1
            if char_map[left_char] == 0:
                del char_map[left_char]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
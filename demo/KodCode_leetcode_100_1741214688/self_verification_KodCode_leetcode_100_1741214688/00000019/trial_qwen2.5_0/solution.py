def smallest_lexicographical_substring(s: str) -> str:
    """
    Returns the lexicographically smallest substring that can be formed by rearranging any number of characters within the string.
    """
    if len(s) <= 1:
        return s
    
    sorted_chars = sorted(s)
    min_char = sorted_chars[0]
    min_substring = s[0]
    
    for i, char in enumerate(s):
        if char == min_char and i > 0 and s[:i].endswith(min_char):
            break
        if char < min_char or (char == min_char and s[i+1:].startswith(min_char)):
            min_char = char
            min_substring = char
    
    # Handle the edge case where the smallest character forms the entire string
    if min_substring == min_char * len(s):
        return min_char
    
    return min_substring + ''.join(sorted(s[len(min_substring):]))
def find_smallest_substring(s: str) -> str:
    """
    Returns the lexicographically smallest substring of the given string.
    """
    if len(s) <= 1:
        return s
    
    # Convert the string into a list to easily sort it
    char_list = sorted(s)
    # The smallest substring will be the first few characters of the sorted list
    min_char = char_list[0]
    
    # Find the starting index of the smallest character in the original string
    start_index = s.index(min_char)
    
    # Try to find the smallest substring starting from the identified character
    smallest_substring = min_char
    for i in range(start_index, len(s)):
        if s[i] < smallest_substring:
            smallest_substring = s[i]
            smallest_start = i
            smallest_end = i + 1
        elif s[i] == smallest_substring:
            # If current character is the same as the smallest, extend the substring
            smallest_end += 1
    
    return s[smallest_start:smallest_end]
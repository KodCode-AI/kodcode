def first_uniq_char(s: str) -> str:
    """
    Finds the first non-repeating character in a string and returns it.
    If there is no such character, returns an underscore ('_').
    """
    char_count = {}
    
    # Counting character occurrences
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Finding the first unique character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return '_'
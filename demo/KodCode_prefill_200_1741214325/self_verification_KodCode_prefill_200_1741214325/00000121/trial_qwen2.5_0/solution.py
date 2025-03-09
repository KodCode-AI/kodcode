def first_unique_char(s: str) -> str:
    """
    Returns the first unique character in the string s.
    If no unique character is found, returns '_'.
    """
    char_count = {}
    
    # Count the occurrence of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first unique character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return '_'
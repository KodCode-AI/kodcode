def can_make_beautiful(s: str) -> bool:
    """
    Returns true if the string s can be made beautiful by performing the specified operation at most once.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    if len(char_count) > 3:
        return False
    
    palindromic = s == s[::-1]
    
    if len(char_count) == 2:
        for char in s:
            char_count[char] -= 1
            if all(v == 0 for v in char_count.values()):
                return True
            char_count[char] += 1
        return palindromic
    
    if len(char_count) == 1:
        return False
    
    # Case where there are exactly 3 characters
    for vowel in vowels:
        if vowel in char_count:
            char_count[vowel] = 0
            if not all(v == 0 for v in char_count.values()):
                return True
            char_count[vowel] = 1
    return palindromic
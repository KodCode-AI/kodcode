def is_isomorphic(s1: str, s2: str) -> bool:
    """
    Checks if two strings are isomorphic.
    """
    if len(s1) != len(s2):
        return False
    
    s1_to_s2 = {}
    s2_to_s1 = {}
    
    for char1, char2 in zip(s1, s2):
        if (char1 in s1_to_s2 and s1_to_s2[char1] != char2) or \
           (char2 in s2_to_s1 and s2_to_s1[char2] != char1):
            return False
        s1_to_s2[char1] = char2
        s2_to_s1[char2] = char1
    
    return True
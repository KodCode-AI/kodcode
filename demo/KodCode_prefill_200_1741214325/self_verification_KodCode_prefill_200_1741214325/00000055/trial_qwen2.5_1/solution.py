def is_isomorphic(s1, s2):
    """
    Checks if two strings are isomorphic. Two strings are isomorphic if the characters in s1 can be replaced to get s2.
    """
    if len(s1) != len(s2):
        return False
    
    s1_to_s2_map = {}
    s2_to_s1_map = {}
    
    for char_from_s1, char_from_s2 in zip(s1, s2):
        if char_from_s1 in s1_to_s2_map:
            if s1_to_s2_map[char_from_s1] != char_from_s2:
                return False
        else:
            s1_to_s2_map[char_from_s1] = char_from_s2
        
        if char_from_s2 in s2_to_s1_map:
            if s2_to_s1_map[char_from_s2] != char_from_s1:
                return False
        else:
            s2_to_s1_map[char_from_s2] = char_from_s1
    
    return True
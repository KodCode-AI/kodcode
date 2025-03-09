def is_isomorphic(s1, s2):
    """
    Returns True if s1 and s2 are isomorphic, otherwise False.
    """
    if len(s1) != len(s2):
        return False
    
    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}
    
    for char_s1, char_s2 in zip(s1, s2):
        if char_s1 in mapping_s1_to_s2:
            if mapping_s1_to_s2[char_s1] != char_s2:
                return False
        else:
            mapping_s1_to_s2[char_s1] = char_s2
        
        if char_s2 in mapping_s2_to_s1:
            if mapping_s2_to_s1[char_s2] != char_s1:
                return False
        else:
            mapping_s2_to_s1[char_s2] = char_s1
    
    return True
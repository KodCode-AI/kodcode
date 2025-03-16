def is_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    s1_map = {}
    s2_map = {}
    
    for c1, c2 in zip(s1, s2):
        if c1 in s1_map:
            if s1_map[c1] != c2:
                return False
        else:
            s1_map[c1] = c2
        
        if c2 in s2_map:
            if s2_map[c2] != c1:
                return False
        else:
            s2_map[c2] = c1
    
    return True
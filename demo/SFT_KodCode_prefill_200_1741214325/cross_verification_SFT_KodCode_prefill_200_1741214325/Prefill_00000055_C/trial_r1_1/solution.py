def is_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    map_s1 = {}
    map_s2 = {}
    for c1, c2 in zip(s1, s2):
        if c1 in map_s1:
            if map_s1[c1] != c2:
                return False
        else:
            if c2 in map_s2:
                return False
            map_s1[c1] = c2
            map_s2[c2] = c1
    return True
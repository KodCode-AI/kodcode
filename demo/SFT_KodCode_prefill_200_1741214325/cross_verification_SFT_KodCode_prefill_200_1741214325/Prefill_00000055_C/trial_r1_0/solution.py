def is_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    map_s1 = {}  # Maps characters from s1 to s2
    map_s2 = {}  # Maps characters from s2 to s1

    for c1, c2 in zip(s1, s2):
        if c1 not in map_s1:
            # Check if c2 is already mapped from another character in s1
            if c2 in map_s2:
                return False
            map_s1[c1] = c2
            map_s2[c2] = c1
        else:
            # Ensure the mapped value is consistent
            if map_s1[c1] != c2:
                return False

    return True
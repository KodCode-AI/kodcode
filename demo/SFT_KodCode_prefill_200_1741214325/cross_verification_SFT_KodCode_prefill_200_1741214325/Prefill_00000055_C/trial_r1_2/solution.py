def is_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True

    def get_pattern(s):
        mapping = {}
        pattern = []
        counter = 0
        for char in s:
            if char not in mapping:
                mapping[char] = counter
                counter += 1
            pattern.append(mapping[char])
        return pattern

    pattern_s1 = get_pattern(s1)
    pattern_s2 = get_pattern(s2)
    return pattern_s1 == pattern_s2
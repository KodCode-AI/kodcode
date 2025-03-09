def min_swaps_to_anagram(s: str, t: str) -> int:
    """
    Returns the minimum number of swaps required to make string s an anagram of string t.
    """
    from collections import Counter
    s_counter, t_counter = Counter(s), Counter(t)
    if s_counter != t_counter:
        return -1  # Early return if s cannot be an anagram of t
    mismatches = [char for char in s if s.count(char) != t.count(char)]
    swaps = 0
    while len(mismatches) > 0:
        for char in mismatches:
            if s.count(char) > t.count(char):
                mismatches.extend([other_char for other_char in t if other_char != char and s.count(other_char) >= t.count(other_char) * 2])
            s.remove(char)
            t.remove(char)
            swaps += 1
            if len(set(s) & set(t)) == len(t) and len(set(s) - set(t)) == 0:
                return swaps
    return swaps
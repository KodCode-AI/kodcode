def min_swaps_to_anagram(s: str, t: str) -> int:
    """
    Returns the minimum number of swaps required to make s an anagram of t.
    """
    from collections import Counter
    s_count, t_count = Counter(s), Counter(t)
    if s_count != t_count:
        return -1  # Impossible to make an anagram if the counts of characters are different
    swaps = 0
    for char in s_count:
        if s_count[char] > t_count[char]:
            swaps += s_count[char] - t_count[char]
    return swaps // 2  # Each pair of mismatched characters requires one swap
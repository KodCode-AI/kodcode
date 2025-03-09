def min_swaps_to_anagram(s, t):
    """
    Returns the minimum number of swaps required to make string s an anagram of string t.
    """
    if len(s) != len(t):
        return -1  # Return -1 if lengths are not equal
    
    # Count the frequency of each character in both strings
    from collections import Counter
    s_count = Counter(s)
    t_count = Counter(t)
    
    # Find characters that are not balanced between the two strings
    imbalance = (s_count - t_count) + (t_count - s_count)
    
    # The minimum number of swaps is half the number of imbalance counts
    return sum(imbalance.values()) // 2
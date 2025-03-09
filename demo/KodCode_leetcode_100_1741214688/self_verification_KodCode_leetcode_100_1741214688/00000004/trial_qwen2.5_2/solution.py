def count_balanced_substrings(s, k):
    """
    Returns the number of balanced substrings in s where the number of distinct
    characters is exactly k.
    """
    i, j = 0, 0
    count, distinct_chars = 0, {}
    while j < len(s):
        distinct_chars[s[j]] = distinct_chars.get(s[j], 0) + 1
        if len(distinct_chars) <= k:
            count += (j - i + 1)
            j += 1
        else:
            while len(distinct_chars) > k:
                distinct_chars[s[i]] -= 1
                if distinct_chars[s[i]] == 0:
                    del distinct_chars[s[i]]
                i += 1
            j += 1
    return count
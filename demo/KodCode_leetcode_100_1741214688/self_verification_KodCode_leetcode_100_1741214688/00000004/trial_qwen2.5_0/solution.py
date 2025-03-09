def count_balanced_substrings(s, k):
    """
    Returns the number of substrings in s where the number of distinct characters is exactly k.
    """
    count = 0
    len_s = len(s)
    for start in range(len_s):
        distinct_chars = set()
        for end in range(start, len_s):
            distinct_chars.add(s[end])
            if len(distinct_chars) == k:
                count += 1
            elif len(distinct_chars) > k:
                break
    return count
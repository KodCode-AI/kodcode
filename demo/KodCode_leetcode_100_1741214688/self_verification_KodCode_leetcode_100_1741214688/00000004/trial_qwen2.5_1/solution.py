def count_balanced_substrings(s, k):
    """
    Returns the number of balanced substrings in s where each substring has exactly k distinct characters.
    """
    from collections import Counter
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(Counter(substring)) == k:
                count += 1
    return count
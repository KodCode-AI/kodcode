def max_good_substrings(s, k):
    """
    Returns the maximum number of good substrings that can be obtained.
    """
    max_good = 0
    current_good = 0
    zeros_count = 0
    for i in range(len(s)):
        if s[i] == '0':
            zeros_count += 1
        if zeros_count > 1:
            zeros_count = 1
            current_good += 1
        max_good = max(max_good, current_good)
        if (i + 1) % (k + 1) == 0 and i < len(s) - 1:
            current_good = 0
    return max_good
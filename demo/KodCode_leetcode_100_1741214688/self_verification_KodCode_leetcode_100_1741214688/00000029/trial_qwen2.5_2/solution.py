def longest_balanced_substring(s, k):
    """
    Returns the length of the longest balanced substring after flipping at most k characters.
    """
    left, num_zeros, max_len = 0, 0, 0
    for right in range(len(s)):
        if s[right] == '0':
            num_zeros += 1
        while right - left + 1 - num_zeros > k:
            if s[left] == '0':
                num_zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
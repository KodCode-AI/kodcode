def longest_balanced_substring(s, k):
    """
    Returns the length of the longest balanced substring that can be
    obtained by flipping at most k characters in the binary string s.
    """
    left = 0
    max_length = 0
    for right in range(len(s)):
        k -= s[right] == '0'  # Flip '0' to '1' and decrease k by 1
        while k < 0:
            k += s[left] == '0'  # Flip '1' to '0' and increase k by 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
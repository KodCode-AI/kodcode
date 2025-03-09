def max_balanced_substring_length(s: str, k: int) -> int:
    """
    Returns the maximum possible length of a balanced substring of s.
    """
    max_length = 0
    balance = 0
    left = 0
    for right in range(len(s)):
        balance += 1 if s[right] == '1' else -1
        while balance < 0:
            balance += 1 if s[left] == '1' else -1
            left += 1
        max_length = max(max_length, right - left + 1 + (2 * k))
    return max_length
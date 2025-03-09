def max_good_substrings(s: str, k: int) -> int:
    """
    Returns the maximum number of good substrings that can be obtained by rearranging
    the characters of s and then splitting the string into at most k non-empty substrings.
    """
    n = len(s)
    counts = [0] * (n + 1)
    for i in range(n):
        counts[i + 1] = counts[i] + (1 if s[i] == '0' else 0)
    
    max_good = 0
    for i in range(min(n, k) + 1):
        if counts[i] > 1:
            break
        mask = (1 << i) - 1
        for j in range(i, n, i + 1):
            if i == 0 or (counts[j + 1] - counts[j - i] > 1):
                mask |= (1 << (j - i + 1))
        max_good = max(max_good, bin(mask).count('1'))
    return max_good
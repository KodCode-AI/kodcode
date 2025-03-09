def max_length_balanced_substring(s: str, k: int) -> int:
    """
    Returns the maximum length of a balanced substring of `s`. A substring is balanced if the frequency of each letter is at most `k`.
    """
    start = 0
    max_len = 0
    freq = {}

    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0) + 1

        while min(freq.values()) > k:
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len
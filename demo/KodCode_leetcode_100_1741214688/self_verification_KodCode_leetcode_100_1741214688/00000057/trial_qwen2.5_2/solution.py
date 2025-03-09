def lexicographically_smallest_string(s: str, k: int) -> str:
    """
    Returns the lexicographically smallest string that can be obtained by reversing any substring of length k.
    """
    n = len(s)
    if k >= n:
        return ''.join(sorted(s))
    
    # Precompute the first character and the lexicographically smallest character
    # that follows each position in the string.
    first_chars = [s[0]] * n
    smallest_after = [s[0]] * n
    for i in range(1, n):
        first_chars[i] = min(first_chars[i-1], s[i])
        smallest_after[i] = min(smallest_after[i-1], s[i] if i < k else s[i-k])

    result = list(s)

    i = n - k
    while i >= 0:
        if s[i] > smallest_after[i]:
            # Find the lexicographically smallest character in the range [i, i+k-1] that is strictly greater than the current character
            j = i
            while j < i + k and s[j] <= s[i]:
                j += 1
            # Swap the found character to position i
            result[i], result[j] = result[j], result[i]
            # Reverse the substring to get the smallest lexicographical order
            result[i+1:i+k+1] = reversed(result[i+1:i+k+1])
        elif s[i] > first_chars[i]:
            # Swap the current character with the smallest character in the range [i, i+k-1] that is strictly greater than the first character of the range
            j = i
            while j < i + k and s[j] == s[i]:
                j += 1
            # Only swap if a different character is found
            if j < i + k and s[j] > first_chars[i]:
                result[i], result[j] = result[j], result[i]
                break
        i -= 1

    return ''.join(result)
def max_balanced_substring_length(s: str, k: int) -> int:
    """
    Returns the maximum length of a balanced substring in s where each letter's frequency is at most k.
    """
    max_length = 0
    start = 0
    frequency = {}
    
    for end in range(len(s)):
        frequency[s[end]] = frequency.get(s[end], 0) + 1
        
        while min(frequency.values()) > k:
            frequency[s[start]] -= 1
            if frequency[s[start]] == 0:
                del frequency[s[start]]
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length
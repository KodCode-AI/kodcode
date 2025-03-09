def max_good_substrings(s, k):
    """
    Returns the maximum number of good substrings that can be obtained by rearranging
    the characters of s and then splitting the string into at most k non-empty substrings.
    """
    ones, zeros = 0, 0
    for char in s:
        if char == '1':
            ones += 1
        else:
            zeros += 1
    
    if zeros <= k:
        return zeros
    else:
        # Split the string at most k times
        splits = 1
        zeros_in_chunk = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_in_chunk += 1
            if zeros_in_chunk > k:
                splits += 1
                zeros_in_chunk = 1  # Reset for the next chunk
            if splits > k:
                break
        
        return min(zeros, splits)
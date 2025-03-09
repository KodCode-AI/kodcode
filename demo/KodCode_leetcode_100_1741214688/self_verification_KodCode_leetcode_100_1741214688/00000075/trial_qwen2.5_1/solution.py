def smallest_by_reversing_substrings(s: str) -> str:
    """
    Returns the lexicographically smallest string by reversing substrings.
    """
    # Initialize an empty list to store intervals of characters
    intervals = []
    start = 0  # Start of the current interval
    
    for i in range(1, len(s)):
        # If the current character is lexicographically smaller than the previous one,
        # it means the current start of the interval is the best start
        if s[i] < s[start]:
            intervals.append((start, i - 1))
            start = i
    intervals.append((start, len(s) - 1))  # Add the last interval
    
    # Reconstruct the string with the smallest lexicographical order
    result = []
    for start, end in intervals:
        result.append(s[start:end + 1][::-1])  # Reverse the interval and add it to the result
    
    return ''.join(result)
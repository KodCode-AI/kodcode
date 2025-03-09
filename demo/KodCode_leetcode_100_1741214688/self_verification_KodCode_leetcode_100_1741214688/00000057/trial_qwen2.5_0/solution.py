def smallest_string_after_reversals(s, k):
    """
    Given a string s and an integer k, return the lexicographically smallest string
    that can be obtained by reversing any substring of length k any number of times.
    """
    # Initialize the result string with the first k characters
    result = s[:k]
    
    # Process the rest of the string in chunks of k
    for i in range(k, len(s), k):
        chunk = s[i:i+k]
        # Reverse the chunk to ensure it's the lexicographically smallest possible
        reversed_chunk = min(chunk, chunk[::-1])
        result += reversed_chunk
    
    # Handle the remaining characters that are less than k
    if len(s) % k != 0:
        result += min(s[-(len(s) % k):], s[-(len(s) % k):][::-1])
    
    return result
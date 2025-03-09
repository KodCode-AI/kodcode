def count_beautiful_substrings(s: str) -> int:
    """
    Returns the number of beautiful substrings in the given string.
    A substring is beautiful if it has an even number of distinct letters and the sum of ASCII values is divisible by 3.
    """
    n = len(s)
    beautiful_count = 0
    
    # Iterate over all possible substrings
    for start in range(n):
        char_count = [0] * 26
        ascii_sum = 0
        distinct_count = 0
        for end in range(start, n):
            index = ord(s[end]) - ord('a')
            char_count[index] += 1
            if char_count[index] == 1: 
                distinct_count += 1
                ascii_sum += ord(s[end])
            elif char_count[index] == 2: 
                ascii_sum -= ord(s[end])
            if distinct_count % 2 == 0 and ascii_sum % 3 == 0:
                beautiful_count += 1
                
    return beautiful_count
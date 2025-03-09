def has_consecutive_repeating_chars(s):
    """
    Returns True if the string contains a sequence of at least two consecutive repeating characters 
    that are not adjacent to each other. Otherwise, returns False.
    """
    if len(s) < 2:
        return False
    
    prev_char = s[0]
    consecutive_count = 1
    
    for char in s[1:]:
        if char == prev_char:
            consecutive_count += 1
        else:
            if consecutive_count >= 2:
                return True
            consecutive_count = 1
        prev_char = char
    
    # Check the last sequence
    return consecutive_count >= 2
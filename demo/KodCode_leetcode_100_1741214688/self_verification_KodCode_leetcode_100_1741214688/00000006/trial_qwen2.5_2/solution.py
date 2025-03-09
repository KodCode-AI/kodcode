def minimal_string(s):
    """
    Returns the lexicographically smallest string that can be obtained by
    performing the allowed operation on the input string `s`.
    """
    # The idea is to move all the 'a's to the front as much as possible.
    # This ensures that the string is as lexicographically small as possible.
    # Search for the first occurrence of 'a' after any occurrence of a non-'a' character.
    min_char = 'a'
    first_index = float('inf')
    for i in range(len(s)):
        if s[i] < min_char:
            min_char = s[i]
            first_index = i
        elif s[i] == min_char and i < first_index:
            first_index = i
    # If 'a' is not the smallest character, search for the first occurrence of the smallest character.
    if min_char != 'a':
        for i in range(len(s)):
            if s[i] == min_char:
                first_index = i
                break
    
    # Reconstruct the string to start with the smallest character as many times as possible.
    left_part = s[:first_index+1]
    # If the string starts with 'a', the result is the string of 'a's and the remaining string.
    if min_char == 'a':
        right_part = s[first_index+1:]
    else:
        # Otherwise, the result is the smallest character and the smallest strings recursively.
        right_part = min_char + minimal_string(s[first_index+1:])
    
    return left_part + right_part
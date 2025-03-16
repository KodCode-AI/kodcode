def reverse_string(s):
    # Convert the string to a list to allow in-place modifications
    s_list = list(s)
    left = 0
    right = len(s_list) - 1
    
    while left < right:
        # Swap characters at left and right pointers
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    # Join the list back into a string
    return ''.join(s_list)
def reverse_string(s):
    """
    Reverses the given string without using extra space.
    
    :param s: The input string to be reversed
    :return: The reversed string
    """
    # Convert string to list of characters since strings are immutable in Python
    str_list = list(s)
    start, end = 0, len(str_list) - 1
    while start < end:
        # Swap characters at start and end positions
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1
    # Convert list of characters back to string
    return ''.join(str_list)
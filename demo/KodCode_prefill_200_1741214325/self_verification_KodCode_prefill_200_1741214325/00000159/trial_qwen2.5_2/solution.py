def reverse_string(s):
    """
    Reverses the given string s without using extra space.
    """
    s = list(s)  # Convert string to list to allow in-place modification
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap characters
        left, right = left + 1, right - 1
    return ''.join(s)  # Convert list back to string
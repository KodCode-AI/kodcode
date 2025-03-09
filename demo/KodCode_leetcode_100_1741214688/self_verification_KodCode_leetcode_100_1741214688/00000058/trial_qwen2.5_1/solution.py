def reverse_segment(s: str, k: int, char: str = 'a') -> str:
    """
    Reverses the segment of s that starts at index 0 and ends at the index of the k-th occurrence of char.
    If char does not occur k times, returns the original string.
    """
    count = 0
    for i, c in enumerate(s):
        if c == char:
            count += 1
        if count == k:
            return s[:i+1][::-1] + s[i+1:]
    return s
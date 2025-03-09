def rotate_string(s, k):
    """
    Rotates the string s by k positions to the right.
    """
    return s[-k:] + s[:-k]

def lexicographically_smallest_string(s, k):
    """
    Returns the lexicographically smallest string that can be obtained
    by rotating the string s at any k indices and the number of such
    operations needed.
    """
    if k >= len(s) or len(set(s)) == 1:
        return s, 1
    
    smallest = s
    min_operations = float('inf')
    
    for i in range(len(s)):
        for _ in range(k):
            s = rotate_string(s, 1)
            if s < smallest:
                smallest = s
                min_operations = 1
            elif s == smallest:
                min_operations += 1
                
    return smallest, min_operations
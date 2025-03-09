def rotate_substring(s, index, k):
    """
    Rotates the substring starting at index by k positions to the right.
    If k is positive, it moves characters to the right; if negative, to the left.
    """
    k = k % len(s)
    return s[index:index+k] + s[index+k:index] + s[:index] if k > 0 else s[index+k:] + s[index:index+k]

def find_smallest_string(s, k):
    """
    Finds the lexicographically smallest string s and the minimum number of operations required.
    """
    n = len(s)
    if k >= n - 1:
        return s, 0
    
    smallest = s
    min_operations = float('inf')
    
    for i in range(n):
        current = s
        operations = 0
        for j in range(n):
            min_index = j
            for r in range(1, k+1):
                rotated = rotate_substring(current, j, r)
                if rotated < current:
                    current = rotated
                    operations += 1
                    min_index = j
                    break
            if min_index == j:
                break
        if current < smallest:
            smallest = current
            min_operations = operations
        s = smallest
    
    return smallest, min_operations
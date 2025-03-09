def min_operations_to_uniform(s: str) -> int:
    """
    Calculates the minimum number of operations required to make the string uniform.
    """
    if len(s) < 2:
        return 0

    min_operations = float('inf')
    for i, j in ((0, s.rfind('a')), (s.find('z'), s.rfind('z'))):
        operations = 0
        while i < j:
            operations += 1
            k = s.rfind('z', i, j)  # Find the last 'z' in the substring s[i..j-1]
            s = s[:i] + s[i:j][::-1] + s[j:]  # Reverse the substring s[i+1..k-1]
            i = k  # Move 'i' to the last 'z'
            j = s.find('a', i + 1)  # Find the next 'a' after 'i'
        if i == j and s[i] == 'a':
            min_operations = min(min_operations, operations)
    if min_operations == float('inf'):
        return -1
    return min_operations
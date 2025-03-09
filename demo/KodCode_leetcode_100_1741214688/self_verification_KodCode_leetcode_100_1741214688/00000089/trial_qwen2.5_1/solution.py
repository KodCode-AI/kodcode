def find_min_string(s: str, k: int) -> (str, int):
    """
    Returns the lexicographically smallest string s that can be obtained after
    performing the rotation operations and the minimum number of operations required.
    """
    if k < len(s):
        rotations = []
        for i in range(len(s)):
            s = s[-1] + s[:-1]  # Rotate the string by one position
            rotations.append((i, 1))
        return s, len(rotations)
    else:
        # If k is large enough, we can make all characters the same with one operation
        # or use up to k-1 operations to make the string lexicographically smallest.
        min_char = min(s)
        for i in range(len(s)):
            if s[i] == min_char:
                return s[i:] + s[:i], 1
        return s, 0  # In case the string is already lexicographically smallest

# Example usage:
# print(find_min_string("bbbaaa", 3))  # Should return ('aaaaabbb', 3)
# print(find_min_string("ccbb", 2))    # Should return ('bbcc', 1)
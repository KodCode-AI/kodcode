def find_lexicographically_largest_palindrome(s):
    """
    Given a string s, find the lexicographically largest palindromic substring.
    """
    n = len(s)
    if n == 0:
        return ""
    
    # Initialize variables to store the result
    start, end = 0, 0
    
    for i in range(n):
        # Check for odd length palindromes
        left, right = expand_around_center(s, i, i)
        if right - left + 1 > end - start + 1:
            start, end = left, right
        
        # Check for even length palindromes
        left, right = expand_around_center(s, i, i + 1)
        if right - left + 1 > end - start + 1:
            start, end = left, right
    
    return s[start:end+1]

def expand_around_center(s, left, right):
    """
    Helper function to expand around the center and find the longest palindrome.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1
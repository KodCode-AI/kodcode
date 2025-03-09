def find_largest_palindrome(s: str) -> str:
    """
    Returns the lexicographically largest palindromic substring in s.
    """
    if not s:
        return ""
    
    max_palindrome = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(max_palindrome):
                max_palindrome = substring
                
    return max_palindrome
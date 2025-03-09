def find_largest_palindromic_substring(s):
    """
    Finds the lexicographically largest palindromic substring in the given string s.
    """
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    largest_palindrome = ""
    for i in range(len(s)):
        # Odd length palindromes
        palindrome_odd = expand_around_center(i, i)
        # Even length palindromes
        palindrome_even = expand_around_center(i, i + 1)
        
        # Update the largest palindrome found
        if len(palindrome_odd) > len(largest_palindrome):
            largest_palindrome = palindrome_odd
        if len(palindrome_even) > len(largest_palindrome):
            largest_palindrome = palindrome_even
    
    return largest_palindrome
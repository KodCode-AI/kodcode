def longest_palindrome_length(s: str) -> int:
    max_length = 0
    n = len(s)
    
    for i in range(n):
        # Check for odd-length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            current_length = r - l + 1
            if current_length > max_length:
                max_length = current_length
            l -= 1
            r += 1
        
        # Check for even-length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            current_length = r - l + 1
            if current_length > max_length:
                max_length = current_length
            l -= 1
            r += 1
    
    return max_length
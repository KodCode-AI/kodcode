def find_largest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    # Create a DP table
    dp = [[False] * n for _ in range(n)]
    
    # Initialize all single characters as palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for two-letter palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    
    # Fill the DP table for lengths >= 3
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
    
    max_length = 0
    max_candidates = []
    
    # Iterate from the longest possible substring to the shortest
    for l in range(n, 0, -1):
        for i in range(n - l + 1):
            j = i + l - 1
            if dp[i][j]:
                candidate = s[i:j+1]
                if l > max_length:
                    max_length = l
                    max_candidates = [candidate]
                elif l == max_length:
                    max_candidates.append(candidate)
        # Early exit as soon as the longest possible substring is found
        if max_length == l:
            break
    
    if not max_candidates:
        return ""
    
    # Return the lexicographically largest substring among candidates
    return max(max_candidates, key=lambda x: x)
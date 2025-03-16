def longest_palindrome_length(s):
    if not s:
        return 0
    max_len = 0
    n = len(s)
    for i in range(n):
        # Check for odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
            l -= 1
            r += 1
        # Check for even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
            l -= 1
            r += 1
    return max_len
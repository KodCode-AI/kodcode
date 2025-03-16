def longest_palindrome(s):
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Calculate the length after expansion

    max_length = 0
    n = len(s)
    for i in range(n):
        # Check for odd length palindromes
        len1 = expand(s, i, i)
        # Check for even length palindromes
        len2 = expand(s, i, i+1)
        current_max = max(len1, len2)
        if current_max > max_length:
            max_length = current_max
    return max_length
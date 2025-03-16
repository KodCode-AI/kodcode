def longest_palindrome_length(s: str) -> int:
    def expand_from_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # After expansion, length is right-left-1

    max_len = 0
    n = len(s)
    for i in range(n):
        # Check for odd length palindromes
        len1 = expand_from_center(i, i)
        # Check for even length palindromes
        len2 = expand_from_center(i, i + 1)
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max

    return max_len
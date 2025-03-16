def longest_palindrome_length(s: str) -> int:
    def expand(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_length = 0
    n = len(s)
    for i in range(n):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        current_max = max(len1, len2)
        if current_max > max_length:
            max_length = current_max
    return max_length
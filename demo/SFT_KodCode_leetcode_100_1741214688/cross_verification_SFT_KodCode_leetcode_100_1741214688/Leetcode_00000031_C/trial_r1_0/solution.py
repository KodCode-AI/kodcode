def find_largest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    max_length = 0
    best_str = ""
    for i in range(n):
        # Odd length
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            current_substring = s[l:r+1]
            current_length = len(current_substring)
            if (current_length > max_length) or (current_length == max_length and current_substring > best_str):
                max_length = current_length
                best_str = current_substring
            l -= 1
            r += 1
        # Even length
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            current_substring = s[l:r+1]
            current_length = len(current_substring)
            if (current_length > max_length) or (current_length == max_length and current_substring > best_str):
                max_length = current_length
                best_str = current_substring
            l -= 1
            r += 1
    return best_str
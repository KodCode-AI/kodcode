def length_of_longest_substring(s):
    if not s:
        return ""
    left = 0
    max_len = 0
    start = 0
    char_index = {}
    for right in range(len(s)):
        char = s[right]
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        current_length = right - left + 1
        if current_length > max_len:
            max_len = current_length
            start = left
    return s[start : start + max_len]
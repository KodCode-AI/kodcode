def length_of_longest_substring(s):
    last_occurrence = {}
    left = 0
    max_len = 0
    start = 0

    for right in range(len(s)):
        char = s[right]
        if char in last_occurrence and last_occurrence[char] >= left:
            left = last_occurrence[char] + 1
        last_occurrence[char] = right
        current_length = right - left + 1
        if current_length > max_len:
            max_len = current_length
            start = left

    return s[start:start + max_len]
def first_repeating_char(s):
    if not s:
        return -1
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in s:
        if freq[char] > 1:
            return char
    return -1
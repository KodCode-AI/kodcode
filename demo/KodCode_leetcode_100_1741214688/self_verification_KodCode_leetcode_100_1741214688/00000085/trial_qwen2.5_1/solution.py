def longest_balanced_substring(s: str) -> int:
    """
    Finds the length of the longest balanced substring in the given string s.
    A balanced substring has an equal number of occurrences for each letter.
    """
    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_balanced(substring):
                max_length = max(max_length, len(substring))
    return max_length

def is_balanced(substring: str) -> bool:
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return all(value == char_count[char] for value in char_count.values())
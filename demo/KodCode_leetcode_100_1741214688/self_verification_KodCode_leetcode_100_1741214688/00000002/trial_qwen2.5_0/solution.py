def beautiful_substrings(s: str) -> int:
    """
    Returns the number of beautiful substrings in the given string s.
    A substring is considered beautiful if it has an even number of distinct characters
    and the sum of ASCII values of all characters in the substring is divisible by 3.
    """
    count = 0
    n = len(s)
    for i in range(n):
        distinct_chars = set()
        ascii_sum = 0
        for j in range(i, n):
            distinct_chars.add(s[j])
            ascii_sum += ord(s[j])
            if len(distinct_chars) % 2 == 0 and ascii_sum % 3 == 0:
                count += 1
    return count
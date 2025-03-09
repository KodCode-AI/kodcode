def count_beautiful_substrings(s: str) -> int:
    """
    Returns the number of beautiful substrings in the given string s.
    A substring is considered beautiful if it has an even number of distinct letters
    and the sum of its ASCII values is divisible by 3.
    """
    def is_beautiful(subs: str) -> bool:
        distinct_chars = set(subs)
        ascii_sum = sum(ord(c) for c in subs)
        return len(distinct_chars) % 2 == 0 and ascii_sum % 3 == 0

    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_beautiful(s[i:j]):
                count += 1
    return count
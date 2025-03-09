def max_by_sorting_substrings(s: str, k: int) -> str:
    """
    Given a string s consisting of lowercase English letters, and an integer k,
    perform up to k operations where each operation consists of choosing a non-empty
    substring and sorting its characters in ascending order. Return the lexicographically
    largest string that can be obtained after performing these operations.
    """
    length = len(s)
    for _ in range(k):
        # Find the last position where a swap can be done to get the lexicographically
        # largest string
        max_pos = -1
        for i in range(length - 1):
            if s[i] < s[i + 1]:
                max_pos = i + 1
        # If no swap can be done, we are done
        if max_pos == -1:
            break
        # Perform the operation on the identified substring
        s = s[:max_pos] + ''.join(sorted(s[max_pos:]))
    return s
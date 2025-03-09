def countGoodSubstrings(s: str) -> int:
    """
    Counts the number of good substrings in the binary string `s`.
    A good substring does not contain leading zeros and has an even length.
    """
    count = 0
    for i in range(len(s) - 1):
        # Check if the substring of length 2 starting at position i is a good substring
        if len(s[i:i+2]) == 2 and s[i] != '0' and s[i+1] != '0':
            count += 1
    return count
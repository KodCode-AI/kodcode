def count_good_substrings(s: str) -> int:
    """
    Counts the number of 'good' substrings in the given binary string 's'.
    A 'good' substring has no leading zeros and has an even length.
    """
    count = 0
    n = len(s)
    for i in range(n):
        # Ensure substring starts with 1
        if s[i] == '1':
            for j in range(i + 1, n, 2):
                if j + 1 < n and s[j+1] == '1':
                    count += 1
                else:
                    break
    return count
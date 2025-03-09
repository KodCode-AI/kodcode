def largest_string(s: str, k: int) -> str:
    """
    Returns the lexicographically largest string obtainable by sorting substrings.
    """
    n = len(s)
    if k == 0:
        return s
    
    # Sort the string in chunks, where each chunk size is as large as possible
    # to maximize the lexicographic order
    chunk_size = n // (k + 1)
    for _ in range(k):
        s = ''.join(sorted(s[i:i + chunk_size] + s[i + chunk_size:i + 2 * chunk_size]) for i in range(0, n - chunk_size + 1))
    return s
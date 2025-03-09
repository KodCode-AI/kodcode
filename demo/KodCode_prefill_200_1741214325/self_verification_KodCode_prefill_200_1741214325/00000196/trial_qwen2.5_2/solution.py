def rabin_karp_search(text, pattern, q=101):
    """
    Returns the starting index of the first occurrence of the
    pattern in the text using the Rabin-Karp algorithm.
    If the pattern is not found, returns -1.
    """
    if len(pattern) == 0 or len(text) < len(pattern):
        return -1

    d = 256  # Number of characters in the input alphabet
    phash = 0  # hash value for pattern
    thash = 0  # hash value for text
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(len(pattern) - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(len(pattern)):
        phash = (d * phash + ord(pattern[i])) % q
        thash = (d * thash + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(len(text) - len(pattern) + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if phash == thash:
            # Check for characters one by one
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i  # pattern found at index i

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < len(text) - len(pattern):
            thash = (d * (thash - ord(text[i]) * h) + ord(text[i + len(pattern)])) % q

            # We might get negative values of thash, converting it to positive
            if thash < 0:
                thash = thash + q

    return -1  # pattern not found
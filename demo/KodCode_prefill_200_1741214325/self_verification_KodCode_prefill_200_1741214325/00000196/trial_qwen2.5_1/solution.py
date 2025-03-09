def rabin_karp_search(text, pattern):
    """
    Searches for a pattern in a given text using the Rabin-Karp algorithm.
    Returns the first index of the pattern in the text, or -1 if not found.
    """
    if len(pattern) == 0 or len(pattern) > len(text):
        return -1

    prime_num = 101
    alphabet_len = 256
    hash_pattern = 0
    hash_text = 0
    h = 1

    # The value of h would be "pow(alphabet_len, M-1)%prime_num"
    for i in range(len(pattern) - 1):
        h = (h * alphabet_len) % prime_num

    # Calculate the hash value of the pattern and first window of text
    for i in range(len(pattern)):
        hash_pattern = (alphabet_len * hash_pattern + ord(pattern[i])) % prime_num
        hash_text = (alphabet_len * hash_text + ord(text[i])) % prime_num

    # Slide the pattern over text one by one
    for i in range(len(text) - len(pattern) + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if hash_pattern == hash_text:
            # Check for characters one by one
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    break
            else:
                # if pattern[0...M-1] = text[i, i+1, ...i+M-1]
                return i

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < len(text) - len(pattern):
            hash_text = (alphabet_len * (hash_text - ord(text[i]) * h) + ord(text[i + len(pattern)])) % prime_num

            # We might get negative values of hash_text, converting it to
            # positive
            if hash_text < 0:
                hash_text = hash_text + prime_num
    return -1
def rabin_karp.search(substring, string):
    """
    Returns the starting index of the first occurrence of substring in string using the Rabin-Karp algorithm.
    If the substring is not found, returns -1.
    """
    if len(substring) == 0 or len(string) == 0 or len(substring) > len(string):
        return -1

    pattern_length = len(substring)
    text_length = len(string)
    prime_num = 101
    alphabet_length = 256
    hash_pattern = 0
    hash_text = 0
    h = 1

    # The value of h would be "pow(alphabet_length, pattern_length-1)%prime_num"
    for i in range(pattern_length-1):
        h = (h * alphabet_length) % prime_num

    # Calculate the hash value of the pattern and first window of text
    for i in range(pattern_length):
        hash_pattern = (alphabet_length * hash_pattern + ord(substring[i])) % prime_num
        hash_text = (alphabet_length * hash_text + ord(string[i])) % prime_num

    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if hash_pattern == hash_text:
            # Check for characters one by one
            for j in range(pattern_length):
                if string[i + j] != substring[j]:
                    break
            else:
                return i  # pattern found at index i

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < text_length - pattern_length:
            hash_text = (alphabet_length * (hash_text - ord(string[i]) * h) + ord(string[i + pattern_length])) % prime_num

            # We might get negative values of hash_text, converting it to
            # positive
            if hash_text < 0:
                hash_text = hash_text + prime_num

    return -1  # pattern not found
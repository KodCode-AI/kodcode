def enhanced_rabin_karp(pattern: str, text: str, alphabet_size: int, modulus: int) -> list:
    if not pattern or not text:
        return []

    # Initialize the variables for the Rabin-Karp algorithm
    pattern_length = len(pattern)
    text_length = len(text)
    hashes = []
    pattern_hash = 0
    current_hash = 0
    h = 1  # The highest power of alphabet_size below modulus

    # If pattern is empty, text is also empty (edge case handled)
    if pattern_length == 0:
        return list(range(pattern_length + 1, text_length + 1))

    # Precompute h = (alphabet_size^(pattern_length-1)) % modulus
    for _ in range(pattern_length - 1):
        h = (h * alphabet_size) % modulus

    # Calculate the hash of the pattern and the first window of the text
    for i in range(pattern_length):
        pattern_hash = (alphabet_size * pattern_hash + ord(pattern[i])) % modulus
        current_hash = (alphabet_size * current_hash + ord(text[i])) % modulus

    # Slide the pattern over text one by one
    indices = []
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == current_hash:
            # Check for characters one by one
            if text[i:i + pattern_length] == pattern:
                indices.append(i)

        # Calculate hash value for the next window of text
        if i < text_length - pattern_length:
            current_hash = (alphabet_size * (current_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % modulus
            current_hash = (current_hash + modulus) % modulus  # To handle negative values

    return indices
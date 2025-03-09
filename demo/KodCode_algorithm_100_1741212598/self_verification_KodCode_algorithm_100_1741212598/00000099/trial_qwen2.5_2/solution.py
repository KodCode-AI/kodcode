def enhanced_rabin_karp(pattern: str, text: str, alphabet_size: int, modulus: int) -> List[int]:
    if not pattern or not text:
        return []
    
    result = []
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1  # The value of h would be "pow(alphabet_size, pattern_length-1)%modulus"
    
    # The initial hash values for pattern and first window of text
    for i in range(pattern_length):
        pattern_hash = (alphabet_size * pattern_hash + ord(pattern[i])) % modulus
        text_hash = (alphabet_size * text_hash + ord(text[i])) % modulus
        if i < pattern_length - 1:
            h = (h * alphabet_size) % modulus
    
    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if pattern_hash == text_hash:
            # Check for characters one by one
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
            else:
                # if pattern[0...R-1] = text[L+1...L+R-1]
                result.append(i)
        
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < text_length - pattern_length:
            text_hash = (alphabet_size * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % modulus
            # We might get negative value of text_hash, converting it to positive
            if text_hash < 0:
                text_hash = text_hash + modulus
            
    return result
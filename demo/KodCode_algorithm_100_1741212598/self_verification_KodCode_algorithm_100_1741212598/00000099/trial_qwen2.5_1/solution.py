from typing import List

def compute_hash(pattern: str, prime: int, modulus: int) -> int:
    hash_value = 0
    p = 256
    for char in pattern:
        hash_value = (hash_value * p + ord(char)) % modulus
    return hash_value

def rabin_karp_search(text: str, pattern: str, alphabet_size: int, modulus: int) -> List[int]:
    result_indices = []
    m = len(pattern)
    n = len(text)
    if m > n:
        return result_indices
    prime = 31  # A prime number to avoid collisions
    hash_pattern = compute_hash(pattern, prime, modulus)
    hash_text = compute_hash(text[:m], prime, modulus)
    
    for i in range(n - m + 1):
        if hash_pattern == hash_text:
            start_index = i
            for j in range(m):
                if text[start_index + j] != pattern[j]:
                    break
            else:
                result_indices.append(start_index)
        if i < n - m:
            hash_text = (hash_text - ord(text[i]) * (prime ** (m - 1))) % modulus
            hash_text = (hash_text * prime + ord(text[i + m])) % modulus
            if hash_text < 0:
                hash_text += modulus
    return result_indices

def enhanced_rabin_karp(pattern: str, text: str, alphabet_size: int, modulus: int) -> List[int]:
    return rabin_karp_search(text, pattern, alphabet_size, modulus)

def test_enhanced_rabin_karp() -> None:
    patterns = ["abc1abc12", "ABABX", "ccc"]
    texts = ["alskfjaldsabc1abc1abc12k23adsfabcabc", "ABABZABABYABABX", "abcabcabc"]
    expected_outputs = [[11, 21], [6], [0, 3, 6]]
    for pattern, text, expected in zip(patterns, texts, expected_outputs):
        assert enhanced_rabin_karp(pattern, text, 256, 1000003) == expected

# Example Usage
test_enhanced_rabin_karp()
from solution import *

from solution import enhanced_rabin_karp

def test_enhanced_rabin_karp() -> None:
    # Test Case 1
    pattern = "abc1abc12"
    text = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    alphabet_size = 256
    modulus = 1000003
    expected_output = [11, 21]
    assert enhanced_rabin_karp(pattern, text, alphabet_size, modulus) == expected_output

    # Test Case 2
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    alphabet_size = 256
    modulus = 1000003
    expected_output = [6]
    assert enhanced_rabin_karp(pattern, text, alphabet_size, modulus) == expected_output

    # Test Case 3
    pattern = "ccc"
    text = "abcabcabc"
    alphabet_size = 256
    modulus = 1000003
    expected_output = [0, 3, 6]
    assert enhanced_rabin_karp(pattern, text, alphabet_size, modulus) == expected_output

    # Test Case 4 (empty pattern)
    pattern = ""
    text = "abcabcabc"
    alphabet_size = 256
    modulus = 1000003
    expected_output = []
    assert enhanced_rabin_karp(pattern, text, alphabet_size, modulus) == expected_output

    # Test Case 5 (empty text)
    pattern = "ccc"
    text = ""
    alphabet_size = 256
    modulus = 1000003
    expected_output = []
    assert enhanced_rabin_karp(pattern, text, alphabet_size, modulus) == expected_output

    print("All test cases passed!")
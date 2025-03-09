from solution import *

def test_length_of_longest_substring():
    assert length_of_longest_substring("eceba") == 3
    assert length_of_longest_substring("ccaabbb") == 5
    assert length_of_longest_substring("aabacbebebe") == 7
    assert length_of_longest_substring("bbaa") == 4
    assert length_of_longest_substring("abcde") == 3
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring("") == 0

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
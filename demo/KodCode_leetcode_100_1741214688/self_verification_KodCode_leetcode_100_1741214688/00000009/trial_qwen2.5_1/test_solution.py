from solution import *

import pytest

def test_max_balanced_substring_length():
    assert max_balanced_substring_length("aacaba", 2) == 3
    assert max_balanced_substring_length("abcaba", 2) == 5
    assert max_balanced_substring_length("bbTickskrqZZttsbr", 5) == 7
    assert max_balanced_substring_length("bbbb", 1) == 1
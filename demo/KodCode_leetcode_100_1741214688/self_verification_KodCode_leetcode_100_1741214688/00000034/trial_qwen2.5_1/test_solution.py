from solution import *

import pytest

def test_count_distinct_palindromic_subsequences():
    assert count_distinct_palindromic_subsequences("abcba") == 7
    assert count_distinct_palindromic_subsequences("cbba") == 5
    assert count_distinct_palindromic_subsequences("aab") == 3
    assert count_distinct_palindromic_subsequences("baac") == 8
    assert count_distinct_palindromic_subsequences("aaaaa") == 33
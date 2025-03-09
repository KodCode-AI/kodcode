from solution import *

import pytest

def test_smallest_lexicographical_substring():
    assert smallest_lexicographical_substring("daily") == "a"
    assert smallest_lexicographical_substring("leetcode") == "e"
    assert smallest_lexicographical_substring("loodecte") == "e"
    assert smallest_lexicographical_substring("aaa") == "aaa"
    assert smallest_lexicographical_substring("zzzzzzzzz") == "z"
    assert smallest_lexicographical_substring("aab") == "aab"
    assert smallest_lexicographical_substring("a") == "a"
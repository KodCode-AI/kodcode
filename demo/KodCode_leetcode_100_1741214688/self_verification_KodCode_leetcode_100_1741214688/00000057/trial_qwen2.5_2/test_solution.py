from solution import *

import pytest

def test_lexicographically_smallest_string():
    assert lexicographically_smallest_string("cbaebabacd", 3) == "abcabad"
    assert lexicographically_smallest_string("edcba", 3) == "cbaed"
    assert lexicographically_smallest_string("aaa", 1) == "aaa"
    assert lexicographically_smallest_string("baaca", 3) == "aaabc"
    assert lexicographically_smallest_string("abab", 2) == "aaba"

def test_edge_cases():
    assert lexicographically_smallest_string("a", 1) == "a"
    assert lexicographically_smallest_string("aa", 2) == "aa"
    assert lexicographically_smallest_string("z", 1) == "z"
    assert lexicographically_smallest_string("zg", 2) == "gz"
    assert lexicographically_smallest_string("zzzzz", 5) == "zzzzz"

def test_non_decreasing_k():
    assert lexicographically_smallest_string("abc", 1) == "abc"
    assert lexicographically_smallest_string("abc", 2) == "acb"
    assert lexicographically_smallest_string("abc", 3) == "abc"
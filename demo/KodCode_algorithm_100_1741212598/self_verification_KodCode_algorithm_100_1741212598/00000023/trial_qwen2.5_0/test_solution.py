from solution import *

import pytest

def test_count_letters():
    assert count_letters(100) == 11
    assert count_letters(342) == 23
    assert count_letters(115) == 20
    assert count_letters(1000) == 11
    assert count_letters(342) == 23
    assert count_letters(115) == 20
    assert count_letters(123) == 20
    assert count_letters(12345) == 19
    assert count_letters(999) == 26
    assert count_letters(1000) == 11

def test_edge_cases():
    assert count_letters(1) == 3
    assert count_letters(0) == 4  # special case for input 0
    assert count_letters(999) == 26
    assert count_letters(1000) == 11

def test_large_numbers():
    for n in range(1, 1001):
        assert count_letters(n) == sum(len(number_to_words(i).replace(" ", "").replace("-", "")) for i in range(1, n + 1))

def test_single_digit():
    for i in range(1, 10):
        assert count_letters(i) == len(ones[i])

def test_tens():
    for i in range(10, 20):
        assert count_letters(i) == len(teens[i - 10])
    for i in range(20, 100):
        if i % 10 != 0:
            assert count_letters(i) == len(tens[i // 10]) + (2 if i % 10 != 0 else 0) + (len(ones[i % 10]) if i % 10 != 0 else 0)
        else:
            assert count_letters(i) == len(tens[i // 10])

def test_hundreds():
    for i in range(100, 1000, 100):
        assert count_letters(i) == len(ones[i // 100]) + 7  # "hundred" + 6 chars for "and"
    for i in range(100, 1000):
        if i % 100 == 0:
            continue
        suffix = '' if i % 100 < 10 else (' and ' + number_to_words(i % 100)) if i % 100 > 0 else ''
        assert count_letters(i) == len(ones[i // 100]) + 7 + (len(suffix) - 3)

def test_thousands():
    for i in range(1000, 10000):
        assert count_letters(i) == count_letters(i // 1000) + 8 + count_letters(i % 1000)
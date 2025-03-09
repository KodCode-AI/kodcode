from solution import *

import pytest

def test_count_trailing_zeros():
    assert count_trailing_zeros(100) == 2
    assert count_trailing_zeros(7) == 0
    assert count_trailing_zeros(1024) == 10
    assert count_trailing_zeros(2048) == 11
    assert count_trailing_zeros(5) == 0

def test_count_trailing_zeros_large_number():
    assert count_trailingzeros(16777216) == 24
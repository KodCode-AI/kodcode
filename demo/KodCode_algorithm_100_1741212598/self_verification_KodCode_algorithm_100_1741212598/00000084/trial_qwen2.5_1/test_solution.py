from solution import *

import pytest

def test_find_min_ratio():
    assert find_min_ratio() == 13

def test_totient_function():
    assert totient(10) == 4
    assert totient(21) == 12
    assert totient(15) == 8

def test_permutation_check():
    assert sorted(str(13)) == sorted(str(totient(13)))
    assert sorted(str(21)) != sorted(str(totient(21)))
    assert sorted(str(15)) != sorted(str(totient(15)))
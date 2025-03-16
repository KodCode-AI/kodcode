from solution import *

import pytest

def test_binomial_coefficient():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(10, 0) == 1
    assert binomial_coefficient(10, 10) == 1
    assert binomial_coefficient(6, 3) == 20
    assert binomial_coefficient(7, 1) == 7
from solution import *

``
from solution import binomial_coefficient

def test_binomial_coefficient():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(10, 3) == 120
    assert binomial_coefficient(0, 0) == 1
    assert binomial_coefficient(6, 0) == 1
    assert binomial_coefficient(6, 6) == 1
    assert binomial_coefficient(6, 1) == 6
    assert binomial_coefficient(6, 5) == 6
    assert binomial_coefficient(3, 3) == 1
    assert binomial_coefficient(3, 1) == 3
    assert binomial_coefficient(3, 2) == 3
    assert binomial_coefficient(7, 4) == 35
    assert binomial_coefficient(9, 4) == 126
    assert binomial_coefficient(12, 5) == 792
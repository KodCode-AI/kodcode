from solution import *

import pytest

def test_efficient_prime_factors():
    assert efficient_prime_factors(10) == [2, 5]
    assert efficient_prime_factors(17) == [17]
    assert efficient_prime_factors(100) == [2, 2, 5, 5]
    assert efficient_prime_factors(30030) == [2, 3, 5, 7, 11, 13]

def test_liouville_lambda():
    assert liouville_lambda(10) == 1
    assert liouville_lambda(11) == -1
    assert liouville_lambda(100) == 1
    assert liouville_lambda(30030) == -1
    with pytest.raises(ValueError):
        liouville_lambda(0)
    with pytest.raises(ValueError):
        liouville_lambda(1.5)
    with pytest.raises(ValueError):
        liouville_lambda(-10)
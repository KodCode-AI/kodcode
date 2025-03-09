from solution import *

import pytest

def test_efficient_prime_factors():
    assert efficient_prime_factors(1) == []
    assert efficient_prime_factors(2) == [2]
    assert efficient_prime_factors(3) == [3]
    assert efficient_prime_factors(18) == [2, 3, 3]
    assert efficient_prime_factors(100) == [2, 2, 5, 5]

def test_liouville_lambda():
    assert liouville_lambda(1) == 1  # 1 has no prime factors
    assert liouville_lambda(2) == -1  # 2 is a prime number
    assert liouville_lambda(10) == 1  # 10 = 2 * 5
    assert liouville_lambda(11) == -1  # 11 is a prime number
    assert liouville_lambda(100) == 1  # 100 = 2 * 2 * 5 * 5
    assert liouville_lambda(30030) == -1  # 30030 = 2 * 3 * 5 * 7 * 11 * 13
    with pytest.raises(ValueError):
        liouville_lambda(-1)
    with pytest.raises(ValueError):
        liouville_lambda(0)

# Additional tests for edge cases and efficiency
def test_large_inputs():
    import random
    for _ in range(10):
        n = random.randint(1, 10**6)
        factors = efficient_prime_factors(n)
        assert len(factors) % 2 == liouville_lambda(n)
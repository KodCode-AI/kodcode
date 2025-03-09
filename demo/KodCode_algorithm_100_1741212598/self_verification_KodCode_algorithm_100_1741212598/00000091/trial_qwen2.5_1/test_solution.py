from solution import *

`
import pytest
from solution import calculate_distinct_prime_factors

def test_calculate_distinct_prime_factors():
    assert calculate_distinct_prime_factors(51242183) == 3
    assert calculate_distinct_prime_factors(123456789) == 2
    assert calculate_distinct_prime_factors(2) == 1  # Prime number
    assert calculate_distinct_prime_factors(221) == 2  # 221 = 13 * 17
    assert calculate_distinct_prime_factors(100) == 2  # 100 = 2^2 * 5^2
    assert calculate_distinct_prime_factors(1) == 0  # Edge case, 1 has no prime factors
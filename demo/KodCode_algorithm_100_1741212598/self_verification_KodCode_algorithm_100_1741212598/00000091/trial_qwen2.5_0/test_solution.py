from solution import *

``
from solution import calculate_distinct_prime_factors

def test_calculate_distinct_prime_factors():
    assert calculate_distinct_prime_factors(51242183) == 3
    assert calculate_distinct_prime_factors(123456789) == 2
    assert calculate_distinct_prime_factors(60) == 3  # 2, 3, 5
    assert calculate_distinct_prime_factors(13) == 1  # Prime number
    assert calculate_distinct_prime_factors(1) == 0
    assert calculate_distinct_prime_factors(2) == 1  # Prime number
    assert calculate_distinct_prime_factors(4) == 1  # 2 is the only prime factor, but we count it once
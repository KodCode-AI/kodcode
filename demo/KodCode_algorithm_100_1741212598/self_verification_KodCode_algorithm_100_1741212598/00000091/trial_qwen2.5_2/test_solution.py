from solution import *

def test_calculate_distinct_prime_factors():
    assert calculate_distinct_prime_factors(51242183) == 3
    assert calculate_distinct_prime_factors(123456789) == 2
    assert calculate_distinct_prime_factors(1) == 0
    assert calculate_distinct_prime_factors(2) == 1
    assert calculate_distinct_prime_factors(100) == 2  # 2 and 5 are the prime factors
    assert calculate_distinct_prime_factors(30) == 3  # 2, 3, and 5 are the prime factors
    assert calculate_distinct_prime_factors(60) == 3  # 2, 3, and 5 are the prime factors
    assert calculate_distinct_prime_factors(1099) == 2  # 7 and 157 are the prime factors

# Test with very large numbers
    assert calculate_distinct_prime_factors(10**6 - 1) == 4  # 109, 3, 3, 7 are prime factors
    assert calculate_distinct_prime_factors(10**6) == 0  # 10^6 is not a prime and has 1 as a factor which is not considered
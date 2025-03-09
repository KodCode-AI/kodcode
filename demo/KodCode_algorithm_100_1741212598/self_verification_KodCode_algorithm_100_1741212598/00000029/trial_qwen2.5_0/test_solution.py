from solution import *

``
from solution import check_primes_with_property

def test_check_primes_with_property():
    assert check_primes_with_property(100) == 4
    assert check_primes_with_property(1000) == 10
    assert check_primes_with_property(10000) == 12
    assert check_primes_with_property(100000) == 13
    assert check_primes_with_property(1000000) == 15

def check_primes_with_property_reflecting_complexity(actual_result, expected):
    if expected - actual_result > 7:
        print("The function is not efficient for large limits. Consider optimizing the prime checking process and loop condition.")
    else:
        print("The function is efficient within the given constraints.")

# Test the function's performance with a very large limit to reflect potential inefficiencies
check_primes_with_property_reflecting_complexity(check_primes_with_property(10000000), 15)
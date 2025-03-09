from solution import *

from solution import find_min_permutation_of_phi, find_min_ratio

def test_find_min_permutation_of_phi():
    assert find_min_permutation_of_phi() == 1393331

def test_phi_with_known_values():
    primes = find_min_ratio().prime_factors(100000)
    assert phi(9, primes) == 6
    assert phi(15, primes) == 8

def test_sieve_of_eratosthenes():
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert find_min_ratio().sieve_of_eratosthenes(30) == expected_primes

def test_find_min_ratio():
    assert 2 <= find_min_ratio() < 10000000
    assert sorted(str(find_min_ratio())) == sorted(str(find_min_ratio().phi(find_min_ratio(), find_min_ratio().prime_factors(100000))))
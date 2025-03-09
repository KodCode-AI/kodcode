from solution import *

``
def test_sieved_of_eratosthenes():
    is_prime = sieve_of_eratosthenes(10)
    assert is_prime == [False, False, True, True, False, True, False, True, False, False, False]

def test_semidivisible_sum():
    assert semidivisible_sum(15) == 30
    assert semidivisible_sum(1000) == 34825
    assert semidivisible_sum(999_966_663_333) == 2480389586872

def test_lps_ups_case():
    is_prime = sieve_of_eratosthenes(isqrt(25) + 1)
    lps, ups = None, None
    for p in range(isqrt(25), 1, -1):
        if is_prime[p]:
            lps = p
            break
    for p in range(isqrt(25), 26):
        if is_prime[p]:
            ups = p
            break
    assert lps == 5
    assert ups == 5

def test_edge_cases():
    assert semidivisible_sum(4) == 4
    assert semidivisible_sum(5) == 5
    assert semidivisible_sum(7) == 7
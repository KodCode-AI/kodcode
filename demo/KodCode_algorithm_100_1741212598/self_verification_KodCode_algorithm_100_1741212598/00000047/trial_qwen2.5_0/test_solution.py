from solution import *

def test_calculate_k():
    assert calculate_k(10, 6) == 5
    assert calculate_k(35, 15) == 58
    assert calculate_k(123, 456) == 268905
    assert calculate_k(0, 5) == 25
    assert calculate_k(-100, 200) == 10000
    assert calculate_k(1000000000, -1000000000) == 7000000000000000000

def test_extended_gcd():
    assert extended_gcd(10, 6) == (2, -1, 2)
    assert extended_gcd(35, 15) == (5, -3, 7)
    assert extended_gcd(0, 5) == (5, 0, 1)
    assert extended_gcd(-100, 200) == (100, -1, 1)
    assert extended_gcd(1000000000, -1000000000) == (1000000000, -1, 1)

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
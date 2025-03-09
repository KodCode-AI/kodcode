from solution import *

from solution import find_mod_inverse, gcd_by_iterative

def test_find_mod_inverse():
    assert find_mod_inverse(3, 11) == 4
    assert find_mod_inverse(17, 3120) == 2753
    assert find_mod_inverse(25, 18) == 11  # Example given in modular inverse tutorial
    assert find_mod_inverse(10, 20) == -1  # This should raise ValueError
    
def test_extended_gcd():
    # Check if the extended_gcd function returns the correct result
    gcd, x, y = extended_gcd(35, 15)
    assert gcd == 5 and x == 1 and y == -2
    
def test_gcd_by_iterative():
    # Check if the gcd_by_iterative function returns the correct result
    assert gcd_by_iterative(35, 15) == 5
    assert gcd_by_iterative(101, 10) == 1

# Testing with different scenarios
def test_case_insensitivity():
    # Should pass without raising ValueError
    assert find_mod_inverse(7, 12) == 7
    assert find_mod_inverse(1107, 2017) == 801

# Handling edge cases
def test_small_modulus():
    # Should handle small modulus correctly
    assert find_mod_inverse(5, 11) == 9

# Testing with known failure case
def test_faulty_input():
    # Raises ValueError as expected
    with pytest.raises(ValueError):
        find_mod_inverse(10, 20)
from solution import *

import pytest

def test_find_min_ratio():
    assert find_min_ratio() == 1393331

# Additional test cases to verify the functionality
def check_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def test_euler_phi():
    assert euler_phi(9) == 6
    assert euler_phi(36) == 12
    assert euler_phi(49) == 42

def test_min_ratio_permutation():
    n = 1393331
    phi_n = euler_phi(n)
    assert check_permutation(n, phi_n)

def test_min_ratio_value():
    n = find_min_ratio()
    phi_n = euler_phi(n)
    assert n == 1393331
    assert check_permutation(n, phi_n)

# Run the tests
if __name__ == "__main__":
    pytest.main()
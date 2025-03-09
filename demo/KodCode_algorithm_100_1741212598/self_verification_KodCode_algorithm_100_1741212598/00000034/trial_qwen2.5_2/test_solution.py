from solution import *

def test_check_opposite_signs():
    assert check_opposite_signs(1, -1) is True
    assert check_opposite_signs(100, 200) is False
    assert check_opposite_signs(-100, -200) is False
    assert check_opposite_signs(0, 1) is True
    assert check_opposite_signs(-1, 0) is False
    assert check_opposite_signs(-1, -1) is False
    assert check_opposite_signs(0, -1) is True
    assert check_opposite_signs(0, 0) is False

# Testing edge cases with very large and very small numbers
assert check_opposite_signs(2**63 - 1, -(2**63)) is True
assert check_opposite_signs(-(2**63), 2**63 - 1) is True
assert check_opposite_signs(0, 2**63 - 1) is True
assert check_opposite_signs(-(2**63), 0) is True
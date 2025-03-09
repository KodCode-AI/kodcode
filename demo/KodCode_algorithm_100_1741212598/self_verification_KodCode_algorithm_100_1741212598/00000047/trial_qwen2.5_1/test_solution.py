from solution import *

import pytest

def test_calculate_k():
    assert calculate_k(10, 6) == 5
    assert calculate_k(35, 15) == 58
    assert calculate_k(221, 143) == 56
    assert calculate_k(-10, 10) == 200
    assert calculate_k(7, 9) == 130
    assert calculate_k(1, 2) == 5
    assert calculate_k(1, 1) == 2
    assert calculate_k(0, 5) == 25

if __name__ == "__main__":
    pytest.main()
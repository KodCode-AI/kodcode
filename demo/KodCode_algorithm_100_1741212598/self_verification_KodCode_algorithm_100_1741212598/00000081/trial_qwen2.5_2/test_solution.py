from solution import *

``
import pytest

def test_optimized_solution():
    assert optimized_solution(1) == 4
    assert optimized_solution(2) == 24
    assert optimized_solution(3) == 64
    assert optimized_solution(4) == 164

if __name__ == "__main__":
    pytest.main()
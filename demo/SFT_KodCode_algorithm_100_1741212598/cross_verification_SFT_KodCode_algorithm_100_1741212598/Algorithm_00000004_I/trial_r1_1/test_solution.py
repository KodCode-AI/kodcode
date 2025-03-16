from solution import *

import pytest

def test_optimized_integer_square_root():
    assert optimized_integer_square_root(15) == 3
    assert optimized_integer_square_root(31) == 5
    assert optimized_integer_square_root(25) == 5
    assert optimized_integer_square_root(1) == 1
    assert optimized_integer_square_root(0) == 0
    assert optimized_integer_square_root(2_147_483_647) == 46340
    with pytest.raises(ValueError):
        optimized_integer_square_root(-1)
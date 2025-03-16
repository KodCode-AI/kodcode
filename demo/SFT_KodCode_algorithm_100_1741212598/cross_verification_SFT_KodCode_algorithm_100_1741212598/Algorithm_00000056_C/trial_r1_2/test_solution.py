from solution import *

import pytest
from typing import List

def test_generate_gray_code():
    assert generate_gray_code(2) == [0, 1, 3, 2]
    assert generate_gray_code(1) == [0, 1]
    assert generate_gray_code(3) == [0, 1, 3, 2, 6, 7, 5, 4]
    assert generate_gray_code(4) == [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]

def test_invalid_input():
    with pytest.raises(ValueError):
        generate_gray_code(0)
    with pytest.raises(ValueError):
        generate_gray_code(-1)
    with pytest.raises(ValueError):
        generate_gray_code(3.5)
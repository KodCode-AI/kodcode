from solution import *

from solution import generate_gray_code

def test_generate_gray_code_positive_numbers():
    assert generate_gray_code(2) == [0, 1, 3, 2]
    assert generate_gray_code(1) == [0, 1]
    assert generate_gray_code(3) == [0, 1, 3, 2, 6, 7, 5, 4]

def test_generate_gray_code_non_positive_numbers():
    with pytest.raises(ValueError):
        generate_gray_code(0)
    with pytest.raises(ValueError):
        generate_gray_code(-1)
    with pytest.raises(ValueError):
        generate_gray_code(0.5)

def test_generate_gray_code_large_numbers():
    assert generate_gray_code(32) == [i for i in range(1 << 32)]
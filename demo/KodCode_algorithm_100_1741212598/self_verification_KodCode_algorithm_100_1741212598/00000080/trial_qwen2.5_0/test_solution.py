from solution import *

import pytest

def test_is_automorphic_number():
    assert is_automorphic_number(76) == True
    assert is_automorphic_number(25) == True
    assert is_automorphic_number(9376) == True
    assert is_automorphic_number(7) == False
    assert is_automorphic_number(-25) == False
    with pytest.raises(TypeError):
        is_automorphic_number(5.0)
    with pytest.raises(TypeError):
        is_automorphic_number("123")
    assert is_automorphic_number(1) == True
    assert is_automorphic_number(6) == True
    assert is_automorphic_number(256) == True
    assert is_automorphic_number(70) == False
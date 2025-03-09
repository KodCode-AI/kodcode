from solution import *

def test_is_automorphic_number():
    assert is_automorphic_number(76) == True
    assert is_automorphic_number(25) == True
    assert is_automorphic_number(9376) == True
    assert is_automorphic_number(7) == False
    assert is_automorphic_number(-25) == False
    try:
        is_automorphic_number(5.0)
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised for non-integer input")


def test_positive_numbers():
    assert is_automorphic_number(1) == False
    assert is_automorphic_number(5) == True
    assert is_automorphic_number(6) == True
    assert is_automorphic_number(25) == True
    assert is_automorphic_number(76) == True

def test_large_automorphic_numbers():
    assert is_automorphic_number(9376) == True
    assert is_automorphic_number(890625) == True

def test_non_automorphic_numbers():
    assert is_automorphic_number(12) == False
    assert is_automorphic_number(13) == False
    assert is_automorphic_number(23) == False

def test_edge_cases():
    assert is_automorphic_number(0) == True
    assert is_automorphic_number(11) == True
    assert is_automorphic_number(100) == False
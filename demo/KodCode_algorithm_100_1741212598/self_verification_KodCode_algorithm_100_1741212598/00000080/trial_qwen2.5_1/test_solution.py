from solution import *

`python
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
    
    # Additional test cases
    assert is_automorphic_number(0) == True
    assert is_automorphic_number(1) == True
    assert is_automorphic_number(6) == True
    assert is_automorphic_number(256) == True
    assert is_automorphic_number(706) == True
    assert is_automorphic_number(2476) == False
    try:
        is_automorphic_number("25")
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised for non-integer input")

# Test with large numbers
assert is_automorphic_number(937600000000000000) == True
assert is_automorphic_number(706000000000000000) == True
assert is_automorphic_number(247600000000000000) == False
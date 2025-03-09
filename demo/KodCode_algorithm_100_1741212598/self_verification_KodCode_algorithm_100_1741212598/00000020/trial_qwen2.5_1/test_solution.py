from solution import *

def test_is_digit_cancelling_fraction():
    assert is_digit_cancelling_fraction(49, 98)
    assert not is_digit_cancelling_fraction(45, 90)
    assert is_digit_cancelling_fraction(16, 64)
    assert is_digit_cancelling_fraction(49, 98)
    assert not is_digit_cancelling_fraction(50, 100)
    assert is_digit_cancelling_fraction(19, 95)  # 1/5

def test_product_of_denominators():
    assert product_of_denominators(2) == 90
    assert product_of_denominators(3) == 100100

# Running the tests
if __name__ == "__main__":
    import pytest
    pytest.main(["-s", "test.py"])
from solution import *

def test_calculate_pi_efficient():
    precision = 50
    expected = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
    result = calculate_pi_efficient(precision)
    assert result == expected

def test_calculate_pi_lower_precision():
    precision = 10
    expected = '3.141592653589793238462643383279502884197169399375'
    result = calculate_pi_efficient(precision)
    assert result == expected

def test_calculate_pi_high_precision():
    precision = 100
    result = calculate_pi_efficient(precision)
    # Here we can only make a partial check because the full result is very long
    assert len(result.split('.')[-1]) == precision
    assert float(result) == float('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899')

def test_calculate_pi_zero_precision():
    precision = 0
    expected = '3'
    result = calculate_pi_efficient(precision)
    assert result == expected
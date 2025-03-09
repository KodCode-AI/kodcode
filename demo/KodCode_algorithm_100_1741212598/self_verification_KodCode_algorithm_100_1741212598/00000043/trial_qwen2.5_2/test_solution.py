from solution import *

import pytest
from decimal import Decimal

def test_calculate_pi_efficient():
    # Test with precision 10
    pi_val_10 = calculate_pi_efficient(10)
    assert pi_val_10 == '3.1415926536'
    
    # Test with precision 50
    pi_val_50 = calculate_pi_efficient(50)
    expected_pi_50 = '3.1415926535897932384626433832795028841971693993751'
    assert pi_val_50 == expected_pi_50
    
    # Test with precision 100
    pi_val_100 = calculate_pi_efficient(100)
    expected_pi_100 = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067'
    assert pi_val_100 == expected_pi_100[:102]  # Cut off at 102 to account for possible rounding

def test_with_large_values():
    large_precision = 200
    pi_val_200 = calculate_pi_efficient(large_precision)
    assert len(pi_val_200) == 203  # Check if the length is correct, considering 2 extra digits for precision
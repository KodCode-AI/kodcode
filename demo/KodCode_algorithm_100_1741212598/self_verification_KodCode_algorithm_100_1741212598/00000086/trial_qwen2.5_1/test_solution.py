from solution import *

``
from solution import electrical_properties

def test_electrical_properties():
    # Calculate inductance given frequency and inductive reactance
    assert electrical_properties(f=1000, x_l=219.9, l=None) == {'inductance': 35.0e-6}
    
    # Calculate frequency given inductance and inductive reactance
    assert electrical_properties(l=35e-6, x_l=219.9, f=None) == {'frequency': 1000.0}
    
    # Calculate inductive reactance given inductance and frequency
    assert electrical_properties(l=35e-6, f=1000, x_l=None) == {'inductive reactance': 219.9}
    
    # Calculate capacitance given frequency and capacitive reactance
    assert electrical_properties(f=1000, x_c=50, c=None) == {'capacitance': 636619.7723675814e-9}
    
    # Example with invalid inputs
    try:
        electrical_properties(f=-1000, x_c=50, c=None)
    except ValueError as e:
        assert str(e) == "Frequency cannot be negative"
    else:
        assert False, "Expected ValueError for negative frequency"
    
    # Test for two None values
    try:
        electrical_properties(f=None, x_l=None, l=None)
    except ValueError as e:
        assert str(e) == "Exactly one property must be None."
    else:
        assert False, "Expected ValueError for more than one None property"

# Run the tests
test_electrical_properties()
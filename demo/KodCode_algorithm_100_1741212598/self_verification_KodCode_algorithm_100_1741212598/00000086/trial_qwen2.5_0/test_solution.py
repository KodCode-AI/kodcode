from solution import *

from solution import electrical_properties

def test_electrical_properties_valid_input():
    # Test calculating inductance given frequency and inductive reactance
    assert electrical_properties(f=1000, x_l=219.9, l=None) == {'inductance': 35.0e-6}
    
    # Test calculating frequency given inductance and inductive reactance
    assert electrical_properties(l=35e-6, x_l=219.9, f=None) == {'frequency': 1000.0}
    
    # Test calculating inductive reactance given inductance and frequency
    assert electrical_properties(l=35e-6, f=1000, x_l=None) == {'inductive reactance': 219.9}
    
    # Test calculating capacitance given frequency and capacitive reactance
    assert electrical_properties(f=1000, x_c=50, c=None) == {'capacitance': 636619.7723675814e-9}

def test_electrical_properties_invalid_input():
    # Invalid input with more than one property as None
    try:
        electrical_properties(l=35e-6, f=1000, x_l=219.9, x_c=None)
    except ValueError as e:
        assert str(e) == "Exactly one property must be None"

    # Invalid input with negative values
    try:
        electrical_properties(l=-35e-6, f=1000, x_l=219.9, x_c=None)
    except ValueError as e:
        assert str(e) == "Invalid input configuration"

    try:
        electrical_properties(l=35e-6, f=-1000, x_l=219.9, x_c=None)
    except ValueError as e:
        assert str(e) == "Frequency cannot be negative"

    try:
        electrical_properties(l=35e-6, f=1000, x_l=-219.9, x_c=None)
    except ValueError as e:
        assert str(e) == "Invalid input configuration"
from solution import *

import pytest

def test_electrical_properties_inductance():
    result = electrical_properties(f=1000.0, x_l=219.9, l=None)
    assert result == {'inductance': 35.0e-6}

def test_electrical_properties_frequency():
    result = electrical_properties(l=35e-6, x_l=219.9, f=None)
    assert result == {'frequency': 1000.0}

def test_electrical_properties_inductive_reactance():
    result = electrical_properties(l=35e-6, f=1000, x_l=None)
    assert result == {'inductive reactance': 219.9}

def test_electrical_properties_capacitance():
    result = electrical_properties(f=1000, x_c=50, c=None)
    assert result == {'capacitance': 636619.7723675814e-9}

def test_electrical_properties_negative_input():
    with pytest.raises(ValueError):
        electrical_properties(f=-1000, x_c=50, c=None)

def test_electrical_properties_more_than_one_none():
    with pytest.raises(ValueError):
        electrical_properties(f=1000, x_c=None, c=None)

def test_electrical_properties_all_properties_given():
    with pytest.raises(ValueError):
        electrical_properties(f=1000, x_c=50, c=636619.7723675814e-9, l=35e-6)
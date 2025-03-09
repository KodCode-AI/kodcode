from solution import *

`python
from solution import calculate_energy_from_mass, calculate_mass_from_energy

def test_calculate_energy_from_mass_positive_numbers():
    assert round(calculate_energy_from_mass(1.0), 15) == 8.987551787368176e+16
    assert round(calculate_energy_from_mass(124.56), 15) == 1.11948945063458e+19
    assert round(calculate_energy_from_mass(0.0), 15) == 0.0

def test_calculate_energy_from_mass_zero():
    assert round(calculate_energy_from_mass(0), 15) == 0.0

def test_calculate_energy_from_mass_negative_numbers():
    with pytest.raises(ValueError):
        calculate_energy_from_mass(-1.0)

def test_calculate_mass_from_energy_positive_numbers():
    assert round(calculate_mass_from_energy(8.987551787368176e+16), 15) == 1.0
    assert round(calculate_mass_from_energy(1.11948945063458e+19), 15) == 124.56
    assert round(calculate_mass_from_energy(0.0), 15) == 0.0

def test_calculate_mass_from_energy_zero():
    assert round(calculate_mass_from_energy(0), 15) == 0.0

def test_calculate_mass_from_energy_negative_numbers():
    with pytest.raises(ValueError):
        calculate_mass_from_energy(-1.0)
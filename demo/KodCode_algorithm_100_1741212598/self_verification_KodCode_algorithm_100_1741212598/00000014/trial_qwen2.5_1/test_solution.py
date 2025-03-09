from solution import *

import math
from solution import calculate_energy_from_mass, calculate_mass_from_energy

def test_calculate_energy_from_mass():
    assert math.isclose(calculate_energy_from_mass(1.0), 8.987551787368176e+16, rel_tol=1e-9)
    assert math.isclose(calculate_energy_from_mass(124.56), 1.11948945063458e+19, rel_tol=1e-9)
    assert math.isclose(calculate_energy_from_mass(0), 0.0, rel_tol=1e-9)

def test_calculate_mass_from_energy():
    assert math.isclose(calculate_mass_from_energy(8.987551787368176e+16), 1.0, rel_tol=1e-9)
    assert math.isclose(calculate_mass_from_energy(1.11948945063458e+19), 124.56, rel_tol=1e-9)
    assert math.isclose(calculate_mass_from_energy(0), 0.0, rel_tol=1e-9)

def test_negative_mass():
    with pytest.raises(ValueError):
        calculate_energy_from_mass(-1.0)

def test_negative_energy():
    with pytest.raises(ValueError):
        calculate_mass_from_energy(-1.0)
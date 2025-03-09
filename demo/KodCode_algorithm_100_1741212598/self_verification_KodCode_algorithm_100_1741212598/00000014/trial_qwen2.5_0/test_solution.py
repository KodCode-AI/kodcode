from solution import *

`python
def test_calculate_energy_from_mass():
    assert round(calculate_energy_from_mass(1.0), 15) == 89875517873681760.0
    assert round(calculate_energy_from_mass(124.56), 15) == 111948945063458048.0
    assert round(calculate_energy_from_mass(0), 15) == 0.0
    with pytest.raises(ValueError):
        calculate_energy_from_mass(-1.0)

def test_calculate_mass_from_energy():
    assert round(calculate_mass_from_energy(89875517873681760.0), 15) == 1.0
    assert round(calculate_mass_from_energy(111948945063458048.0), 15) == 124.56
    assert round(calculate_mass_from_energy(0), 15) == 0.0
    with pytest.raises(ValueError):
        calculate_mass_from_energy(-1.0)

def test_large_values():
    large_value = 1e-30
    assert round(calculate_energy_from_mass(large_value), 15) == 0.0
    assert round(calculate_mass_from_energy(1e-60), 15) == 0.0

def test_small_values():
    small_value = 1e30
    assert round(calculate_energy_from_mass(small_value), 15) == 89875517873681760.0
    assert round(calculate_mass_from_energy(89875517873681760000000000000000000.0), 15) == small_value
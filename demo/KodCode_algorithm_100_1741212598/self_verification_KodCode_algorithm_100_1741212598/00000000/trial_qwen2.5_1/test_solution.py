from solution import *

import pytest

def test_energy_conversion_joule_to_electronvolt():
    assert pytest.approx(energy_conversion("joule", "electronvolt", 1e-15)) == 6.241509074460763e+15
    assert pytest.approx(energy_conversion("electronvolt", "joule", 1e-15)) == 1.602176634e-19

def test_energy_conversion_electronvolt_per_photon_to_joule():
    assert pytest.approx(energy_conversion("electronvolt_per_photon", "joule", 1)) == 6.241509074460763e+15
    assert pytest.approx(energy_conversion("joule", "electronvolt_per_photon", 6.241509074460763e+15)) == 1.0

def test_energy_conversion_electronvolt_per_photon_to_wattsecond():
    assert pytest.approx(energy_conversion("electronvolt_per_photon", "wattsecond", 1)) == 0.00016402208664101444
    assert pytest.approx(energy_conversion("wattsecond", "electronvolt_per_photon", 0.00016402208664101444)) == 1.0

def test_energy_conversion_wattsecond_to_joule():
    assert pytest.approx(energy_conversion("wattsecond", "joule", 1)) == 1.0
    assert pytest.approx(energy_conversion("joule", "wattsecond", 1)) == 1.0

def test_energy_conversion_invalid_units():
    with pytest.raises(ValueError, match="Invalid unit: from watt to joule. Supported units are"):
        energy_conversion("watt", "joule", 1)
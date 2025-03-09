from solution import *

def test_energy_conversion():
    assert energy_conversion("electronvolt_per_photon", "joule", 1) == 6.241509074460763e+15
    assert energy_conversion("joule", "electronvolt_per_photon", 6.241509074460763e+15) == 1.0
    assert energy_conversion("electronvolt_per_photon", "wattsecond", 1) == 0.00016402208664101444
    assert energy_conversion("wattsecond", "electronvolt_per_photon", 0.00016402208664101444) == 1.0
    assert energy_conversion("joule", "joule", 10.0) == 10.0
    assert energy_conversion("wattsecond", "wattsecond", 5.0) == 5.0
    assert energy_conversion("electronvolt_per_photon", "electronvolt_per_photon", 2.0) == 2.0
    
    # Test error handling
    try:
        energy_conversion("unknown_unit", "joule", 1)
    except ValueError as e:
        assert str(e) == "Invalid units provided. Supported units: ['joule', 'wattsecond', 'electronvolt_per_photon']"

    try:
        energy_conversion("joule", "unknown_unit", 1)
    except ValueError as e:
        assert str(e) == "Invalid units provided. Supported units: ['joule', 'wattsecond', 'electronvolt_per_photon']"
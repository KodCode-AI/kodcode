from solution import *

def test_energy_conversion():
    # Basic conversions
    assert abs(energy_conversion("electronvolt", "joule", 1) - 1.602176634e-19) < 1e-10
    assert abs(energy_conversion("joule", "electronvolt_per_photon", 6.241509074460763e+15) - 1.0) < 1e-10
    assert abs(energy_conversion("wattsecond", "joule", 1) - 1.0) < 1e-10
    assert abs(energy_conversion("joule", "wattsecond", 1.0) - 1.0) < 1e-10

    # Conversion with electronvolt_per_photon
    assert abs(energy_conversion("electronvolt_per_photon", "wattsecond", 1) - 0.00016402208664101444) < 1e-10
    assert abs(energy_conversion("wattsecond", "electronvolt_per_photon", 0.00016402208664101444) - 1.0) < 1e-10

    # Error handling
    try:
        energy_conversion("invalid_unit", "joule", 1)
    except ValueError as e:
        assert str(e) == "Invalid unit conversion from invalid_unit to joule"

    try:
        energy_conversion("joule", "invalid_unit", 1)
    except ValueError as e:
        assert str(e) == "Invalid unit conversion from joule to invalid_unit"

    try:
        energy_conversion("invalid_unit", "invalid_unit", 1)
    except ValueError as e:
        assert str(e) == "Invalid unit conversion from invalid_unit to invalid_unit"

test_energy_conversion()
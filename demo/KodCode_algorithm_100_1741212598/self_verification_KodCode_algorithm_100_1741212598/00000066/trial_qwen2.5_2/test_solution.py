from solution import *

import pytest

def test_simulate_555_timer():
    # Test with positive values
    result = simulate_555_timer(resistance_1=45, resistance_2=45, capacitance=7)
    assert 'error' not in result
    assert result['frequency'] == pytest.approx(1523809.5238095239, rel=1e-2)
    assert result['duty_cycle'] == pytest.approx(66.66666666666666, rel=1e-2)
    assert result['details'] == 'Frequency: 1.44 / [(45 + 2 * 45) * 7] * 10^6 = 1523809.5238095239 Hz, Duty Cycle: (45 + 45) / (45 + 2 * 45) * 100 = 66.66666666666666 %'

    # Test with floating point precision
    result = simulate_555_timer(resistance_1=356, resistance_2=234, capacitance=976)
    assert 'error' not in result
    assert result['frequency'] == pytest.approx(1790.5459175553078, rel=1e-2)
    assert result['duty_cycle'] == pytest.approx(71.60194174757282, rel=1e-2)
    assert result['details'] == 'Frequency: 1.44 / [(356 + 2 * 234) * 976] * 10^6 = 1790.5459175553078 Hz, Duty Cycle: (356 + 234) / (356 + 2 * 234) * 100 = 71.60194174757282 %'

    # Test with negative values
    result = simulate_555_timer(resistance_1=-1, resistance_2=45, capacitance=7)
    assert result == {'error': 'All values must be positive'}

    # Test with zero values
    result = simulate_555_timer(resistance_1=0, resistance_2=0, capacitance=0)
    assert result == {'error': 'All values must be positive'}
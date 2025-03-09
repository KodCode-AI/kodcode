from solution import *

import pytest

def test_simulate_555_timer_positive_numbers():
    result = simulate_555_timer(45, 45, 7)
    assert isinstance(result, dict)
    assert 'frequency' in result
    assert 'duty_cycle' in result
    assert 'details' in result
    assert result['frequency'] == 1523809.5238095239
    assert result['duty_cycle'] == 66.66666666666666
    assert result['details'] == 'Frequency: 1.44 / [( 45 + 2 * 45 ) * 7] * 10^6 = 1523809.5238095239 Hz, Duty Cycle: ( 45 + 45 ) / ( 45 + 2 * 45 ) * 100 = 66.66666666666666 %'

def test_simulate_555_timer_negative_values():
    result = simulate_555_timer(-1, 45, 7)
    assert result == {'error': 'All values must be positive'}

def test_simulate_555_timer_zero_values():
    result = simulate_555_timer(0, 45, 7)
    assert result == {'error': 'All values must be positive'}

def test_simulate_555_timer_mixed_values():
    result = simulate_555_timer(356, 234, 976)
    assert result['frequency'] == 1790.5459175553078
    assert result['duty_cycle'] == 71.60194174757282
    assert result['details'] == 'Frequency: 1.44 / [( 356 + 2 * 234 ) * 976] * 10^6 = 1790.5459175553078 Hz, Duty Cycle: ( 356 + 234 ) / ( 356 + 2 * 234 ) * 100 = 71.60194174757282 %'
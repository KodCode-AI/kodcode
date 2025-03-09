from solution import *

from solution import simulate_555_timer

def test_simulate_555_timer_positive_values():
    result = simulate_555_timer(45, 45, 7)
    assert result == {
        'frequency': 1523809.5238095239,
        'duty_cycle': 66.66666666666666,
        'details': 'Frequency: 1.44 / [(45 + 2 * 45) * 7] * 10^6 = 1523809.5238095239 Hz, Duty Cycle: (45 + 45) / (45 + 2 * 45) * 100 = 66.66666666666666 %'
    }

def test_simulate_555_timer_large_values():
    result = simulate_555_timer(356, 234, 976)
    assert result == {
        'frequency': 1790.5459175553078,
        'duty_cycle': 71.60194174757282,
        'details': 'Frequency: 1.44 / [(356 + 2 * 234) * 976] * 10^6 = 1790.5459175553078 Hz, Duty Cycle: (356 + 234) / (356 + 2 * 234) * 100 = 71.60194174757282 %'
    }

def test_simulate_555_timer_negative_value():
    result = simulate_555_timer(-1, 45, 7)
    assert result == {'error': 'All values must be positive'}

def test_simulate_555_timer_zero_values():
    result = simulate_555_timer(0, 0, 0)
    assert result == {'error': 'All values must be positive'}
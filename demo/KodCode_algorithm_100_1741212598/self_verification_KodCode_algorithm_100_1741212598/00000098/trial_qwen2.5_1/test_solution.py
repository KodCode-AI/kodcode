from solution import *

import pytest

def test_terminal_velocity_positive_values():
    assert round(terminal_velocity(0.5, 750, 0.05, 0.47), 10) == 1.6416094135
    assert round(terminal_velocity(1, 1000, 0.1, 0.5), 10) == 1.9843136661

def test_terminal_velocity_zero_value():
    with pytest.raises(ValueError):
        terminal_velocity(0.5, 750, 0.05, 0.47)
        terminal_velocity(0, 750, 0.05, 0.47)
        terminal_velocity(0.5, 0, 0.05, 0.47)
        terminal_velocity(0.5, 750, 0, 0.47)
        terminal_velocity(0.5, 750, 0.05, 0)

def test_terminal_velocity_negative_values():
    with pytest.raises(ValueError):
        terminal_velocity(-0.5, 750, 0.05, 0.47)
        terminal_velocity(0.5, -750, 0.05, 0.47)
        terminal_velocity(0.5, 750, -0.05, 0.47)
        terminal_velocity(0.5, 750, 0.05, -0.47)

def test_terminal_velocity_out_of_range():
    with pytest.raises(ValueError):
        terminal_velocity(1001, 750, 0.05, 0.47)
        terminal_velocity(0.5, 1001, 0.05, 0.47)
        terminal_velocity(0.5, 750, 0.00099, 0.47)
        terminal_velocity(0.5, 750, 0.05, 0.099)
from solution import *

``
import pytest

def test_terminal_velocity_positive_values():
    result = terminal_velocity(0.5, 750, 0.05, 0.47)
    assert round(result, 8) == 1.6416094135332785

def test_terminal_velocity_positive_values_2():
    result = terminal_velocity(1, 1000, 0.1, 0.5)
    assert round(result, 8) == 1.9843136660766868

def test_terminal_velocity_zero_mass():
    with pytest.raises(ValueError, match="All input parameters must be positive."):
        terminal_velocity(0, 750, 0.05, 0.47)

def test_terminal_velocity_zero_density():
    with pytest.raises(ValueError, match="All input parameters must be positive."):
        terminal_velocity(0.5, 0, 0.05, 0.47)

def test_terminal_velocity_zero_area():
    with pytest.raises(ValueError, match="All input parameters must be positive."):
        terminal_velocity(0.5, 750, 0, 0.47)

def test_terminal_velocity_zero_drag_coefficient():
    with pytest.raises(ValueError, match="All input parameters must be positive."):
        terminal_velocity(0.5, 750, 0.05, 0)

def test_terminal_velocity_min_values():
    result = terminal_velocity(1, 1, 0.001, 0.1)
    assert round(result, 8) == 1.9843136660766868

def test_terminal_velocity_max_values():
    result = terminal_velocity(1000, 1000, 1, 1)
    assert round(result, 8) == 31.30495168499705

def test_terminal_velocity_mixed_sign_values():
    with pytest.raises(ValueError, match="All input parameters must be positive."):
        terminal_velocity(-1, 750, 0.05, 0.47)
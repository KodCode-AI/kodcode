from solution import *

``
from solution import terminal_velocity

def test_terminal_velocity_positive_values():
    assert round(terminal_velocity(0.5, 750, 0.05, 0.47), 5) == 1.64161

def test_terminal_velocity_large_values():
    assert round(terminal_velocity(1, 1000, 0.1, 0.5), 5) == 1.98431

def test_terminal_velocity_edge_values():
    assert round(terminal_velocity(1, 1000, 0.001, 1), 5) == 4.90476
    assert round(terminal_velocity(1000, 1, 1, 0.1), 5) == 39.49327

def test_terminal_velocity_zero_input():
    try:
        terminal_velocity(0, 1000, 0.05, 0.47)
        assert False, "Expected ValueError for zero mass"
    except ValueError as e:
        assert str(e) == "All inputs must be positive and non-zero."
    
    try:
        terminal_velocity(1, 0, 0.05, 0.47)
        assert False, "Expected ValueError for zero density"
    except ValueError as e:
        assert str(e) == "All inputs must be positive and non-zero."

    try:
        terminal_velocity(1, 1000, 0, 0.47)
        assert False, "Expected ValueError for zero area"
    except ValueError as e:
        assert str(e) == "All inputs must be positive and non-zero."

    try:
        terminal_velocity(1, 1000, 0.05, 0)
        assert False, "Expected ValueError for zero drag coefficient"
    except ValueError as e:
        assert str(e) == "All inputs must be positive and non-zero."
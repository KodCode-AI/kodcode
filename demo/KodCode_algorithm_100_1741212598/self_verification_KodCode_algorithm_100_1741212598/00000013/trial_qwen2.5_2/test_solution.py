from solution import *

import pytest

def test_manhattan_distance_improved():
    # Test with positive and integer coordinates
    assert manhattan_distance_improved([1, 1], [2, 2]) == 2.0
    assert manhattan_distance_improved([1.5, 1.5], [2, 2]) == 1.0
    assert manhattan_distance_improved([1.5, 1.5], [2.5, 2]) == 1.5
    assert manhattan_distance_improved([-3, -3, -3], [0, 0, 0]) == 9.0

    # Test with edge cases
    with pytest.raises(TypeError):
        manhattan_distance_improved([1, 1], None)

    with pytest.raises(ValueError):
        manhattan_distance_improved([1, 1], [2, 2, 2])

    with pytest.raises(TypeError):
        manhattan_distance_improved([1, "one"], [2, 2, 2])

# Test with pytest
if __name__ == "__main__":
    pytest.main([__file__])
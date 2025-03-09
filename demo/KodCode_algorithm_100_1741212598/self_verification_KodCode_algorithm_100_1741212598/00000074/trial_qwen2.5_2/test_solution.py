from solution import *

python
def count_reversible_numbers(max_power: int) -> int:
    if max_power == 1:
        return 5
    counts = [0] * (max_power + 1)
    counts[1] = 5
    for i in range(2, max_power + 1):
        if i % 2 == 0:
            half_power = i // 2
            counts[i] = 5 * 5 * 5 * 2
        else:
            half_power = (i - 1) // 2
            counts[i] = 5 * 5 * 5 * 5
    return counts[max_power]

# Unit Tests
def test_count_reversible_numbers():
    assert count_reversible_numbers(1) == 5
    assert count_reversible_numbers(2) == 5 * 5 * 2
    assert count_reversible_numbers(3) == 5 * 5 * 5 * 5
    assert count_reversible_numbers(4) == 5 * 5 * 5 * 2
    assert count_reversible_numbers(5) == 5 * 5 * 5 * 5
    assert count_reversible_numbers(6) == 5 * 5 * 5 * 2
    assert count_reversible_numbers(7) == 5 * 5 * 5 * 5
    assert count_reversible_numbers(8) == 5 * 5 * 5 * 2
    assert count_reversible_numbers(9) == 5 * 5 * 5 * 5

test_count_reversible_numbers()
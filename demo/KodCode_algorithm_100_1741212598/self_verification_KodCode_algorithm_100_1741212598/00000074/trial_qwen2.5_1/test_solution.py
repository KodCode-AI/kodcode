from solution import *

import pytest

@lru_cache(None)
def is_reversible(num: int) -> bool:
    str_num = str(num)
    if str_num[0] == '0':  # Leading zero is not allowed
        return False
    for i in range(len(str_num)):
        if (int(str_num[i]) in [0, 2, 4, 6, 8]) and (i != len(str_num) - 1):
            return False
    for i in range(len(str_num) // 2):
        if (int(str_num[i]) + int(str_num[~i]) in [0, 2, 4, 6, 8]):
            return False
    return True

def count_reversible_numbers(max_power: int) -> int:
    total_count = 0
    for length in range(1, max_power + 1):
        if length == 1:
            total_count += 5  # Single digit: 1, 3, 5, 7, 9
        elif length % 2 == 1:
            counts = [0] * 10
            for i in [1, 3, 5, 7, 9]:
                counts[i] = 1
            for _ in range(length // 2):
                new_counts = [0] * 10
                for i in [1, 3, 5, 7, 9]:
                    for j in [1, 3, 5, 7, 9]:
                        new_counts[(i + j) % 10] += counts[i]
                counts = new_counts
            total_count += sum(counts[i] for i in [1, 3, 5, 7, 9]) * 5
        else:
            counts = [0] * 10
            for i in [1, 3, 5, 7, 9]:
                counts[i] = 1
            for _ in range(length // 2 - 1):
                new_counts = [0] * 10
                for i in [1, 3, 5, 7, 9]:
                    for j in [1, 3, 5, 7, 9]:
                        if is_reversible((i * 10 + j) % 100):
                            new_counts[(i + j) % 10] += counts[i]
                counts = new_counts
            total_count += sum(counts[i] for i in [1, 3, 5, 7, 9]) * 5 * 2
    return total_count

def test_count_reversible_numbers():
    assert count_reversible_numbers(3) == 120
    assert count_reversible_numbers(6) == 18720
    assert count_reversible_numbers(7) == 68720
    assert count_reversible_numbers(1) == 5
    assert count_reversible_numbers(2) == 45

test_count_reversible_numbers()
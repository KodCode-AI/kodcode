from solution import *

from solution import generate_combinations
import itertools

def test_generate_combinations():
    numbers = [1, 2, 3]
    expected_combinations = list(itertools.chain.from_iterable(itertools.combinations(numbers, r) for r in range(1, len(numbers) + 1)))
    assert sorted(generate_combinations(numbers)) == sorted(expected_combinations)

def test_generate_combinations_empty_list():
    numbers = []
    expected_combinations = []
    assert generate_combinations(numbers) == expected_combinations

def test_generate_combinations_single_element():
    numbers = [1]
    expected_combinations = [(), (1,)]
    assert sorted(generate_combinations(numbers)) == sorted(expected_combinations)
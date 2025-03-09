from solution import *

from solution import generate_combinations

def test_generate_combinations_with_empty_list():
    assert generate_combinations([]) == [()],

def test_generate_combinations_with_single_element():
    assert generate_combinations([1]) == [(), (1,)]

def test_generate_combinations_with_multiple_elements():
    expected_output = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    assert generate_combinations([1, 2, 3]) == expected_output

def test_generate_combinations_with_repeated_elements():
    expected_output = [
        (), (1,), (2,), (3,), 
        (1, 1), (1, 2), (1, 3), 
        (2, 2), (2, 3), 
        (3, 3),
        (1, 1, 1), (1, 1, 2), (1, 1, 3), 
        (1, 2, 2), (1, 2, 3), 
        (1, 3, 3), 
        (2, 2, 2), (2, 2, 3), 
        (2, 3, 3), 
        (3, 3, 3),
        (1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), 
        (1, 1, 2, 2), (1, 1, 2, 3), 
        (1, 1, 3, 3), 
        (1, 2, 2, 2), (1, 2, 2, 3), 
        (1, 2, 3, 3), 
        (1, 3, 3, 3), 
        (2, 2, 2, 2), (2, 2, 2, 3), 
        (2, 2, 3, 3), 
        (2, 3, 3, 3), 
        (3, 3, 3, 3), 
        (1, 1, 1, 1, 1)
    ]
    assert generate_combinations([1, 1, 2, 2, 3]) == expected_output

def test_generate_combinations_with_negative_values():
    expected_output = [(), (-1,), (-2,), (3,), (-1, -2), (-1, 3), (-2, 3), (-1, -2, 3)]
    assert generate_combinations([-1, -2, 3]) == expected_output
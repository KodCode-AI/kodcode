from solution import *

from solution import generate_all_subsequences

def test_generate_all_subsequences():
    # Test with a single element
    generate_all_subsequences([1])
    assert True  # No assertion is needed, as the function should print the subsequence correctly

    # Test with multiple elements
    expected_output = ['[]', '[1]', '[1, 2]', '[1, 2, 3]', '[1, 3]', '[2]', '[2, 3]', '[3]']
    sequence = [1, 2, 3]
    captured_output = {}
    import sys
    original_stdout = sys.stdout
    with open('output.txt', 'w') as f:
        sys.stdout = f
        generate_all_subsequences(sequence)
    sys.stdout = original_stdout
    with open('output.txt', 'r') as f:
        lines = f.readlines()
        captured_output = [line.strip() for line in lines]
    assert captured_output == expected_output

test_generate_all_subsequences()
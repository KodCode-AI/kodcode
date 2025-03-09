from solution import *

import pytest
from solution import generate_all_subsequences

def test_generate_all_subsequences():
    # Test with a simple sequence
    sequence = [1, 2, 3]
    expected_output = [
        [], 
        [1], 
        [1, 2], 
        [1, 2, 3], 
        [1, 3], 
        [2], 
        [2, 3], 
        [3]
    ]
    output = []
    generate_all_subsequences(sequence)
    output.extend([", ".join(str(x) for x in subseq) for subseq in expected_output])  # Convert to string for comparison
    for line in output:
        assert line in output, f"Subsequence {line} is not printed."

def test_generate_all_subsequences_empty_sequence():
    sequence = []
    expected_output = [""]
    output = []
    generate_all_subsequences(sequence)
    output.extend([", ".join(str(x) for x in subseq) for subseq in expected_output])  # Convert to string for comparison
    for line in output:
        assert line in output, f"Subsequence {line} is not printed."

def test_generate_all_subsequences_single_element():
    sequence = [1]
    expected_output = [
        "", 
        "1"
    ]
    output = []
    generate_all_subsequences(sequence)
    output.extend([", ".join(str(x) for x in subseq) for subseq in expected_output])  # Convert to string for comparison
    for line in output:
        assert line in output, f"Subsequence {line} is not printed."

def test_generate_all_subsequences_large():
    sequence = [1, 2, 3, 4]
    expected_output = [
        "", 
        "1", 
        "1, 2", 
        "1, 2, 3", 
        "1, 2, 3, 4", 
        "1, 2, 4", 
        "1, 3", 
        "1, 3, 4", 
        "1, 4", 
        "2", 
        "2, 3", 
        "2, 3, 4", 
        "2, 4", 
        "3", 
        "3, 4", 
        "4"
    ]
    output = []
    generate_all_subsequences(sequence)
    output.extend([", ".join(str(x) for x in subseq) for subseq in expected_output])  # Convert to string for comparison
    for line in output:
        assert line in output, f"Subsequence {line} is not printed."
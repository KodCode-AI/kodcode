from solution import *

import pytest
from typing import *
from solution import generate_all_subsequences

def test_generate_all_subsequences():
    sequence = [1, 2, 3]
    expected_output = ['[]', '[1]', '[1, 2]', '[1, 2, 3]', '[1, 3]', '[2]', '[2, 3]', '[3]']
    
    # Capture the print output
    from io import StringIO
    import sys
    captured_output = StringIO()
    sys.stdout = captured_output
    generate_all_subsequences(sequence)
    sys.stdout = sys.__stdout__
    
    # Convert the captured output to a list of strings
    output_lines = captured_output.getvalue().splitlines()
    
    # Assert that each line in the expected output is contained in the actual output
    for line in expected_output:
        assert line in output_lines
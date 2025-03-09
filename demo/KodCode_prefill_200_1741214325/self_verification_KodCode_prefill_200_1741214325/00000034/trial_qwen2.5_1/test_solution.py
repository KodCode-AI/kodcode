from solution import *

from solution import print_primes

def test_print_primes():
    test_cases = [
        (5, "2\n3\n5\n"),
        (11, "2\n3\n5\n7\n11\n"),
        (2, "2\n"),
        (0, ""),
        (1, ""),
        (19, "2\n3\n5\n7\n11\n13\n17\n19\n")
    ]
    
    for input_num, expected_output in test_cases:
        with print_function_capturing() as output:
            print_primes(input_num)
        assert output.getvalue().strip() == expected_output

import sys
from contextlib import redirect_stdout

def print_function_capturing():
    class StringIO:
        def __init__(self):
            self.string = ""

        def write(self, content):
            self.string += content

        def getvalue(self):
            return self.string

    return StringIO()
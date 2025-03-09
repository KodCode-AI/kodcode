from solution import *

from solution import print_primes

def test_print_primes_small_number():
    print_primes(10)  # Should print: 2, 3, 5, 7

def test_print_primes_large_number():
    captured_output = capture_printed_output(print_primes, 50)
    expected_output = "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37\n41\n43\n47\n"
    assert captured_output == expected_output

def test_print_primes_no_primes():
    captured_output = capture_printed_output(print_primes, 2)
    assert captured_output == ""

def test_print_primes_empty_input():
    captured_output = capture_printed_output(print_primes, 1)
    assert captured_output == ""

# Helper function to capture printed output
def capture_printed_output(func, *args, **kwargs):
    from io import StringIO
    import sys
    original_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    func(*args, **kwargs)
    
    sys.stdout = original_stdout
    return captured_output.getvalue().strip()
from solution import *

from solution import print_primes, is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(29) == True
    assert is_prime(49) == False

def test_print_primes():
    start, end = 10, 20
    expected_primes = [11, 13, 17, 19]
    with capture_stdout() as stdout:
        print_primes(start, end)
    printed_primes = stdout.getvalue().strip().split('\n')
    assert all(map(lambda x: is_prime(int(x)), printed_primes))
    assert set(printed_primes) == set(map(str, expected_primes))

def test_invalid_range():
    try:
        print_primes(10, 5)
        assert False, "Expected ValueError not raised for invalid range."
    except ValueError:
        assert True

def test_edge_cases():
    start, end = 2, 2
    with capture_stdout() as stdout:
        print_primes(start, end)
    printed_output = stdout.getvalue().strip()
    assert printed_output == str(start)
    
def test_with_no_primes():
    start, end = 8, 8
    with capture_stdout() as stdout:
        print_primes(start, end)
    printed_output = stdout.getvalue().strip()
    assert printed_output == ''  # No output because there are no primes in the given range.
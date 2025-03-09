from solution import *

from solution import print_primes

def test_print_primes():
    # Test with a known prime number up to 10
    import io
    import contextlib
    with contextlib.redirect_stdout(io.StringIO()) as output:
        print_primes(10)
        result = output.getvalue().strip()
    assert result == '2 3 5 7 ', f"Expected '2 3 5 7 ', got '{result}'"
    
    # Test with 2, which is the smallest prime number
    with contextlib.redirect_stdout(io.StringIO()) as output:
        print_primes(2)
        result = output.getvalue().strip()
    assert result == '2 ', f"Expected '2 ', got '{result}'"
    
    # Test with a larger number
    with contextlib.redirect_stdout(io.StringIO()) as output:
        print_primes(30)
        result = output.getvalue().strip()
    assert result == '2 3 5 7 11 13 17 19 23 29 ', f"Expected '2 3 5 7 11 13 17 19 23 29 ', got '{result}'"
    
    # Test with 1, which should print nothing
    with contextlib.redirect_stdout(io.StringIO()) as output:
        print_primes(1)
        result = output.getvalue().strip()
    assert result == '', f"Expected '', got '{result}'"
from solution import *

from solution import print_prime_numbers, is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(25) == False
    assert is_prime(29) == True

def test_print_prime_numbers():
    # Check a simple range
    with test_output_capture() as output:
        print_prime_numbers(10, 20)
    assert output.getvalue().strip().split("\n") == ["11", "13", "17", "19"]

    # Check an empty range
    with test_output_capture() as output:
        print_prime_numbers(15, 15)
    assert output.getvalue().strip() == ""

    # Check validating for range inclusivity and lower limit
    with test_output_capture() as output:
        print_prime_numbers(2, 3)
    assert output.getvalue().strip().split("\n") == ["2", "3"]

    # Check large range with primes at both ends
    with test_output_capture() as output:
        print_prime_numbers(100, 110)
    assert output.getvalue().strip().split("\n") == ["101", "103", "107", "109"]

def test_prime_with_negativeranges():
    # Handling negative ranges and ensuring no negative primes printed
    with test_output_capture() as output:
        print_prime_numbers(-5, 1)
    assert output.getvalue().strip() == "2"

    with test_output_capture() as output:
        print_prime_numbers(-10, -5)  # This should not print any primes
    assert output.getvalue().strip() == ""
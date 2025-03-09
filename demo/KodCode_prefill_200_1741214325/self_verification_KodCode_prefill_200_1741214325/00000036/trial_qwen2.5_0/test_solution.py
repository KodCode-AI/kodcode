from solution import *

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(121) == False  # 121 is not a prime
    assert is_prime(15485863) == True  # 15485863 is a large prime number

def test_print_primes():
    # Using a non-printing output method to simulate the print behavior
    output = []
    original_print = print

    def log(msg):
        output.append(msg)

    print = log

    start = 1
    end = 10
    print_primes(start, end)
    print = original_print

    expected_output = [2, 3, 5, 7]
    assert output == [2, 3, 5, 7]

    # Testing with a larger range
    start = 10
    end = 20
    print_primes(start, end)
    expected_output = [11, 13, 17, 19]
    assert output == [11, 13, 17, 19]

    # Test with no primes in the range
    start = 23
    end = 29
    print_primes(start, end)
    expected_output = []
    assert output == []
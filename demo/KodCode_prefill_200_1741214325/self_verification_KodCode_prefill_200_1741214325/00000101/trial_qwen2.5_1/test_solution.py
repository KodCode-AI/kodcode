from solution import *

def test_print_numbers():
    # Test with a simple list of numbers
    with capture_stdout(print_numbers, [1, 2, 3]) as output:
        assert output == "1\n2\n3\n"

    # Test with an empty list
    with capture_stdout(print_numbers, []) as output:
        assert output == ""

    # Test with a list containing a single number
    with capture_stdout(print_numbers, [42]) as output:
        assert output == "42\n"
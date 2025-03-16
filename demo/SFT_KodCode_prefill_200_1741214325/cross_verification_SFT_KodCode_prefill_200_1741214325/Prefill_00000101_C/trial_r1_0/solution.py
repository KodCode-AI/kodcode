from typing import List
import io
import contextlib

def print_numbers(numbers: List[int]) -> None:
    """ Iterates over a list and prints each number. """
    for num in numbers:
        print(num)

def test_print_numbers():
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        print_numbers([1, 2, 3, 4, 5])
    output = captured_output.getvalue().strip().split('\n')
    assert output == ['1', '2', '3', '4', '5']

def test_print_numbers_with_empty_list():
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        print_numbers([])
    output = captured_output.getvalue().strip()
    assert output == ''
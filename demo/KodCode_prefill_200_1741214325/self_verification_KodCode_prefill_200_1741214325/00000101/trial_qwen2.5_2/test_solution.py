from solution import *

def test_print_numbers():
    with test_script capturing print output as output:
        print_numbers([1, 2, 3])
    assert output == '1\n2\n3\n'

def test_empty_list():
    with test_script capturing print output as output:
        print_numbers([])
    assert output == ''

def test_mixed_sign_numbers():
    with test_script capturing print output as output:
        print_numbers([-1, 0, 1])
    assert output == '-1\n0\n1\n'
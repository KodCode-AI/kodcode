from solution import *

``
def test_collatz_sequence_length():
    assert collatz_sequence_length(13) == 10
    assert collatz_sequence_length(1) == 1

def test_find_longest_collatz_sequence():
    assert find_longest_collatz_sequence(1000000) == 837799
    assert find_longest_collatz_sequence(500) == 371
    assert find_longest_collatz_sequence(100) == 97
    assert find_longest_collatz_sequence(10) == 9
    assert find_longest_collatz_sequence(10000) == 6171
    assert find_longest_collatz_sequence(50000) == 37117
from solution import *

from solution import find_longest_collatz_sequence, collatz_sequence_length

def test_collatz_sequence_length():
    assert collatz_sequence_length(13) == 10
    assert collatz_sequence_length(7) == 17
    assert collatz_sequence_length(35) == 154
    assert collatz_sequence_length(626331) == 351

def test_find_longest_collatz_sequence():
    assert find_longest_collatz_sequence(10) == 9
    # Example given in the problem statement
    assert find_longest_collatz_sequence(1000000) == 837799
    # Additional test cases
    assert find_longest_collatz_sequence(1000) == 871
    assert find_longest_collatz_sequence(10000) == 6372
    assert find_longest_collatz_sequence(100000) == 83779

# Run the tests
import pytest
pytest.main([__file__])
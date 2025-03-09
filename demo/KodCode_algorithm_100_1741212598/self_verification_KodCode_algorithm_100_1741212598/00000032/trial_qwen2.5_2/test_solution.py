from solution import *

def test_collatz_sequence_length():
    assert collatz_sequence_length(1) == 1
    assert collatz_sequence_length(2) == 2
    assert collatz_sequence_length(5) == 6

def test_find_longest_collatz_sequence():
    assert find_longest_collatz_sequence(10) == 9
    assert find_longest_collatz_sequence(1000) == 871
    assert find_longest_collatz_sequence(1000000) == 837799

def test_collatz_sequence_performance():
    limit = 1000000
    result = find_longest_collatz_sequence(limit)
    # Note: The exact expected value for 1000000 is expected based on the known results.
    # This test is more about verifying the performance and correctness.
    assert result == 837799
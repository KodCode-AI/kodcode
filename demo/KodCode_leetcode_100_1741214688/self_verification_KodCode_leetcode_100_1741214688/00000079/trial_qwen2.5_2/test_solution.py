from solution import *

def test_range_freq_query():
    arr = [1, 2, 2, 3, 3, 3, 4]
    freq_query = RangeFreqQuery(arr)

    assert freq_query.query(0, 6, 3) == 3
    assert freq_query.query(2, 5, 2) == 2
    assert freq_query.query(0, 6, 1) == 1

    # Additional tests
    assert freq_query.query(3, 6, 3) == 2
    assert freq_query.query(0, 2, 2) == 2
    assert freq_query.query(4, 6, 4) == 1

test_range_freq_query()
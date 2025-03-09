from solution import *

from solution import RangeFreqQuery

def test_range_freq_query_positive():
    arr = [1, 2, 2, 3, 3, 3, 4]
    rfq = RangeFreqQuery(arr)
    assert rfq.query(0, 6, 3) == 3
    assert rfq.query(0, 6, 2) == 2

def test_range_freq_query_with_overlap():
    arr = [2, 4, 1, 2, 3, 2]
    rfq = RangeFreqQuery(arr)
    assert rfq.query(0, 5, 2) == 3

def test_range_freq_query_empty_range():
    arr = [2, 2, 2, 2]
    rfq = RangeFreqQuery(arr)
    assert rfq.query(3, 2, 2) == 0

def test_range_freq_query_without_element():
    arr = [1, 1, 1, 2, 2, 2, 3]
    rfq = RangeFreqQuery(arr)
    assert rfq.query(0, 6, 4) == 0

def test_range_freq_query_single_element():
    arr = [5, 5, 5, 5, 5]
    rfq = RangeFreqQuery(arr)
    assert rfq.query(0, 4, 5) == 5

def test_range_freq_query_high_frequency():
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    rfq = RangeFreqQuery(arr)
    assert rfq.query(0, 9, 1) == 10
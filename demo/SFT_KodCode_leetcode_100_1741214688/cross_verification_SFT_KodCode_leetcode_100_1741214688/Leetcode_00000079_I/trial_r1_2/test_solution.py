from solution import *

import pytest
from solution import RangeFreqQuery

def test_range_freq_query_positive():
    arr = [1, 2, 2, 3, 3, 3, 4]
    freq_query = RangeFreqQuery(arr)
    assert freq_query.query(0, 6, 3) == 3
    assert freq_query.query(0, 2, 2) == 2
    assert freq_query.query(3, 6, 4) == 1

def test_range_freq_query_empty_subarray():
    arr = [1, 2, 2, 3, 3, 3, 4]
    freq_query = RangeFreqQuery(arr)
    assert freq_query.query(4, 4, 1) == 0

def test_range_freq_query_single_value():
    arr = [1, 1, 1, 1, 1, 1, 1]
    freq_query = RangeFreqQuery(arr)
    assert freq_query.query(0, 6, 1) == 7

def test_range_freq_query_no_occurrence():
    arr = [1, 2, 3, 4, 5, 6, 7]
    freq_query = RangeFreqQuery(arr)
    assert freq_query.query(0, 6, 8) == 0

def test_range_freq_query_negative_numbers():
    arr = [-1, -2, -2, -3, -3, -3, -4]
    freq_query = RangeFreqQuery(arr)
    assert freq_query.query(0, 6, -3) == 3
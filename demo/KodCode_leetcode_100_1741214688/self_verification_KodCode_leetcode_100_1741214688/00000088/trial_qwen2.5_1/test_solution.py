from solution import *

import pytest

interval_manager = IntervalManager()

def test_add_merge():
    interval_manager.addInterval(1, 3)
    interval_manager.addInterval(2, 6)
    interval_manager.addInterval(8, 10)
    interval_manager.addInterval(15, 18)
    assert interval_manager.mergeIntervals() == [[1, 6], [8, 10], [15, 18]]
    interval_manager.addInterval(5, 7)
    assert interval_manager.mergeIntervals() == [[1, 7], [8, 10], [15, 18]]

def test_remove_merge():
    interval_manager.addInterval(1, 4)
    interval_manager.addInterval(4, 5)
    interval_manager.removeInterval(1, 4)
    assert interval_manager.mergeIntervals() == [[4, 5]]
    interval_manager.addInterval(6, 8)
    assert interval_manager.mergeIntervals() == [[4, 5], [6, 8]]

def test_query():
    interval_manager.addInterval(1, 3)
    interval_manager.addInterval(5, 9)
    assert interval_manager.queryInterval(2, 4)
    assert not interval_manager.queryInterval(4, 5)
    assert interval_manager.queryInterval(5, 7)
    assert interval_manager.queryInterval(7, 9)
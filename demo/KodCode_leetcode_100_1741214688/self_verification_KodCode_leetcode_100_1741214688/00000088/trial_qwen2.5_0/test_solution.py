from solution import *

from solution import IntervalManager, Interval

def test_addInterval():
    manager = IntervalManager()
    manager.addInterval(1, 2)
    manager.addInterval(3, 4)
    manager.addInterval(5, 6)
    assert manager.mergeIntervals() == [Interval(1, 2), Interval(3, 4), Interval(5, 6)]

def test_removeInterval():
    manager = IntervalManager()
    manager.addInterval(1, 10)
    manager.addInterval(2, 5)
    manager.removeInterval(2, 5)
    assert manager.mergeIntervals() == [Interval(1, 1), Interval(5, 10)]

def test_mergeIntervals():
    manager = IntervalManager()
    manager.addInterval(1, 5)
    manager.addInterval(3, 7)
    manager.addInterval(8, 10)
    assert manager.mergeIntervals() == [Interval(1, 7), Interval(8, 10)]

def test_queryInterval():
    manager = IntervalManager()
    manager.addInterval(1, 10)
    manager.addInterval(5, 8)
    assert manager.queryInterval(6, 7) == True
    assert manager.queryInterval(2, 3) == True
    assert manager.queryInterval(11, 15) == False
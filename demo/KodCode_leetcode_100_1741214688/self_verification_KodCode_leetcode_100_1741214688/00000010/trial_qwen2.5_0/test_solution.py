from solution import *

from solution import IntervalManager

def test_interval_manager():
    manager = IntervalManager()
    manager.addInterval(1, 3)
    manager.addInterval(6, 9)
    assert manager.getIntervals() == [[1, 3], [6, 9]]

    manager.addInterval(2, 5)
    assert manager.getIntervals() == [[1, 5], [6, 9]]

    manager.mergeOverlappingIntervals()
    assert manager.getIntervals() == [[1, 5], [6, 9]]

    manager.removeInterval(1, 5)
    assert manager.getIntervals() == [[6, 9]]

    manager.addInterval(15, 18)
    manager.addInterval(10, 12)
    assert manager.getIntervals() == [[6, 9], [10, 12], [15, 18]]

    manager.removeInterval(10, 11)
    assert manager.getIntervals() == [[6, 9], [11, 12], [15, 18]]
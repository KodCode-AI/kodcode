from solution import *

def test_interval_manager():
    manager = IntervalManager()
    manager.addInterval(1, 3)
    manager.addInterval(2, 6)
    manager.addInterval(8, 10)
    manager.addInterval(15, 18)
    assert manager.getIntervals() == [[1, 6], [8, 10], [15, 18]]
    
    manager.removeInterval(1, 4)
    assert manager.getIntervals() == [[5, 6], [8, 10], [15, 18]]
    
    manager.removeInterval(15, 17)
    assert manager.getIntervals() == [[5, 6], [8, 10]]
    
    manager.addInterval(10, 12)
    assert manager.getIntervals() == [[5, 6], [8, 12]]
    
    manager.mergeOverlappingIntervals()
    assert manager.getIntervals() == [[5, 12]]
from solution import *

def test_interval_manager():
    manager = IntervalManager()

    # Add intervals
    manager.addInterval(1, 2)
    manager.addInterval(3, 4)
    manager.addInterval(5, 7)
    assert manager.queryInterval(2, 3) == True
    assert manager.queryInterval(1, 1) == True
    assert manager.queryInterval(4, 4) == True
    assert manager.queryInterval(7, 8) == True
    assert manager.queryInterval(0, 0) == False

    # Remove interval
    manager.removeInterval(3, 4)
    assert manager.queryInterval(2, 3) == False
    assert manager.queryInterval(3, 3) == False

    # Merge intervals
    assert manager.mergeIntervals() == [[1, 2], [5, 7]]

    # Add interval that overlaps but does not merge
    manager.addInterval(3, 10)
    assert manager.mergeIntervals() == [[1, 2], [3, 10], [5, 7]]

    # Add and merge adjacent intervals
    manager.addInterval(2, 3)
    assert manager.mergeIntervals() == [[1, 3], [5, 7], [10, 10]]

    # Add and merge over multiple intervals
    manager.addInterval(8, 8)
    manager.addInterval(9, 9)
    assert manager.mergeIntervals() == [[1, 3], [5, 7], [8, 10]]

    # Complex queries and interval manipulation
    manager.addInterval(0, 10)
    assert manager.queryInterval(0, 0) == True
    assert manager.queryInterval(0, 1) == True
    assert manager.queryInterval(6, 10) == True
    assert manager.queryInterval(12, 15) == False
   (manager.removeInterval(12, 15) not in manager.intervals)

test_interval_manager()
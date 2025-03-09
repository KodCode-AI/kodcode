from solution import *

def test_interval_manager():
    interval_manager = IntervalManager()
    interval_manager.addInterval(1, 3)
    interval_manager.addInterval(2, 6)
    interval_manager.addInterval(8, 10)
    interval_manager.addInterval(15, 18)
    assert interval_manager.getIntervals() == [[1, 6], [8, 10], [15, 18]]

    merged_intervals = interval_manager.mergeOverlappingIntervals()
    assert merged_intervals == [[1, 6], [8, 10], [15, 18]], f"Expected [[1, 6], [8, 10], [15, 18]] but got {merged_intervals}"

    interval_manager.removeInterval(3, 6)
    assert interval_manager.getIntervals() == [[8, 10], [15, 18]], f"Expected [[8, 10], [15, 18]] but got {interval_manager.getIntervals()}"

    interval_manager.addInterval(10, 11)
    assert interval_manager.getIntervals() == [[8, 11], [15, 18]], f"Expected [[8, 11], [15, 18]] but got {interval_manager.getIntervals()}"

    merged_intervals = interval_manager.mergeOverlappingIntervals()
    assert merged_intervals == [[8, 11], [15, 18]], f"Expected [[8, 11], [15, 18]] but got {merged_intervals}"

    interval_manager.addInterval(9, 12)
    assert interval_manager.getIntervals() == [[8, 12], [15, 18]], f"Expected [[8, 12], [15, 18]] but got {interval_manager.getIntervals()}"

    merged_intervals = interval_manager.mergeOverlappingIntervals()
    assert merged_intervals == [[8, 18]], f"Expected [[8, 18]] but got {merged_intervals}"
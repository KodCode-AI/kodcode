def min_intervals_to_remove(intervals):
    """
    Finds the minimum number of intervals to remove in order for the remaining
    intervals not to overlap.
    """
    if not intervals:
        return 0
    
    # Sort intervals based on the end time
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1   # Count of non-overlapping intervals
    
    for interval in intervals[1:]:
        if interval[0] >= end:
            count += 1
            end = interval[1]
    
    # The number of intervals to remove is the total number of intervals
    # minus the number of non-overlapping intervals
    return len(intervals) - count
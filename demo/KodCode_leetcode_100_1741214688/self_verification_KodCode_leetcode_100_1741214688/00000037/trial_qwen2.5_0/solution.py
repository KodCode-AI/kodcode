def min_intervals_to_remove(intervals):
    """
    Given a list of intervals, find the minimum number of intervals to remove
    so that the remaining intervals do not overlap.
    """
    if len(intervals) <= 1:
        return 0
    
    # Sort intervals based on the end point. If two intervals have the same end point, sort by start point
    intervals.sort(key=lambda x: (x[1], x[0]))
    
    last_end = intervals[0][1]
    count = 0
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:
            count += 1
        else:
            last_end = intervals[i][1]
    
    return count
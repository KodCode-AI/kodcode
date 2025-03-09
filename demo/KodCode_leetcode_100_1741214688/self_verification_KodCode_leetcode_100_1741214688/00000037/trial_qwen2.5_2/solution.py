def min_intervals_to_remove(intervals):
    """
    Finds the minimum number of intervals to remove so that no two remaining intervals overlap.
    """
    if not intervals:
        return 0
    
    # Sort intervals based on their end times
    intervals.sort(key=lambda x: x[1])
    
    end = intervals[0][1]
    count = 1  # We will keep at least one interval before removing any
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
            
    return len(intervals) - count
from bisect import bisect_left, bisect_right
from itertools import chain

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (self.start, self.end) == (other.start, other.end)

    def __lt__(self, other):
        return self.start < other.start or (self.start == other.start and self.end < other.end)

class IntervalManager:
    def __init__(self):
        self.intervals = []
        self._add_queue = []

    def addInterval(self, start, end):
        new_interval = Interval(start, end)
        
        # Remove intervals if the new interval overlaps with any of them
        start_index = bisect_right(self.intervals, new_interval, key=lambda x: x.end)
        end_index = bisect_left(self.intervals, new_interval, key=lambda x: x.start)
        
        self.intervals = self.intervals[:start_index] + [new_interval] + self.intervals[end_index:]
        self._add_queue = []

    def removeInterval(self, start, end):
        interval_to_remove = Interval(start, end)
        
        # Find and remove the interval
        index = bisect_left(self.intervals, interval_to_remove)
        if index < len(self.intervals) and self.intervals[index] == interval_to_remove:
            self.intervals.pop(index)

    def mergeIntervals(self):
        merged_intervals = []
        for interval in self.intervals:
            if merged_intervals and merged_intervals[-1].end >= interval.start - 1:
                merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
            else:
                merged_intervals.append(interval)
        return merged_intervals

    def queryInterval(self, start, end):
        query_interval = Interval(start, end)
        return bisect_right(self.intervals, query_interval, key=lambda x: x.end) > bisect_left(self.intervals, query_interval, key=lambda x: x.start)
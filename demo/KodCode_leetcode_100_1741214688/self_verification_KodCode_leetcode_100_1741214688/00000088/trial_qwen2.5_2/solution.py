from typing import List

class IntervalManager:
    def __init__(self):
        self.intervals = []
    
    def addInterval(self, start: int, end: int) -> None:
        # This function will add a new interval if it does not overlap with any existing interval
        new_interval = [start, end]
        # Insert the new interval in a sorted manner
        idx = 0
        while idx < len(self.intervals) and new_interval[0] > self.intervals[idx][1]:
            idx += 1
        if idx < len(self.intervals) and new_interval[0] < self.intervals[idx][1]:
            # New interval overlaps with existing one, do not add
            return
        elif idx > 0 and self.intervals[idx-1][1] >= new_interval[0]:
            # New interval overlaps with the interval just before the insertion point, merge them
            self.intervals[idx-1][1] = max(self.intervals[idx-1][1], end)
            if idx < len(self.intervals) and self.intervals[idx][0] <= self.intervals[idx-1][1]:
                # Merge with the next interval as well if applicable
                self.intervals[idx-1][1] = max(self.intervals[idx-1][1], self.intervals[idx][1])
                self.intervals.pop(idx)
        else:
            # No overlap found, insert the new interval
            self.intervals.insert(idx, new_interval)
    
    def removeInterval(self, start: int, end: int) -> None:
        # This function will remove an existing interval if it exists
        self.intervals = [interval for interval in self.intervals if interval[1] < start or interval[0] > end]
    
    def mergeIntervals(self) -> List[int]:
        # Merge all overlapping intervals
        if not self.intervals:
            return []
        
        merged = [self.intervals[0]]
        for interval in self.intervals[1:]:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged
    
    def queryInterval(self, start: int, end: int) -> bool:
        # Query if there is any interval that overlaps with the given interval
        for interval in self.intervals:
            if interval[0] <= end and interval[1] >= start:
                return True
        return False
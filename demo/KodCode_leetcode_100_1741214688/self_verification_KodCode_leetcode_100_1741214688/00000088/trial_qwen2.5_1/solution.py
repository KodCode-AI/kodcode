from typing import List

class IntervalManager:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start: int, end: int) -> None:
        intervals = self.intervals
        new_interval = [start, end]
        insert_pos = -1
        
        # Find the insert position to ensure intervals remain sorted
        for i, interval in enumerate(intervals):
            if end < interval[0]:
                insert_pos = i
                break
        else:
            insert_pos = len(intervals)
        
        inserted = False
        for i, interval in enumerate(intervals):
            if i == insert_pos:
                # Check for overlapping intervals and merge if necessary
                if start <= interval[0]:
                    if end < interval[0]:
                        # Fully to the left
                        pass
                    elif end < interval[1]:
                        # Partial overlap on the right
                        new_interval[1] = interval[1]
                        insert_pos = i + 1
                        inserted = True
                        break
                    elif end >= interval[1]:
                        # Complete overlap or extends right
                        new_interval = interval
                        inserted = True
                        continue
                elif start > interval[0]:
                    # No overlap
                    if end < interval[0]:
                        # Fully to the right
                        pass
                    else:
                        # Overlap from the left
                        new_interval[0] = interval[0]
                        insert_pos = i
                        inserted = True
                        break
                else:
                    # Start is equal to interval[0]; cannot happen since insert_pos is found
                    assert False
            intervals[i] = new_interval
        if not inserted:
            intervals.insert(insert_pos, new_interval)

    def removeInterval(self, start: int, end: int) -> None:
        self.intervals = [interval for interval in self.intervals if interval != [start, end]]

    def mergeIntervals(self) -> List[int:]:
        if not self.intervals:
            return []
        
        merged = []
        current = self.intervals[0]
        for interval in self.intervals[1:]:
            if interval[0] <= current[1]:
                current[1] = max(current[1], interval[1])
            else:
                merged.append(current)
                current = interval
        merged.append(current)
        self.intervals = merged
        return self.intervals

    def queryInterval(self, start: int, end: int) -> bool:
        intervals = self.intervals
        for interval in intervals:
            if interval[0] <= end and interval[1] >= start:
                return True
        return False
from typing import List

class IntervalManager:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start: int, end: int) -> None:
        intervals = self.intervals
        if not intervals or intervals[-1][1] < start - 1:
            intervals.append([start, end])
        elif intervals[0][0] > end + 1:
            intervals.insert(0, [start, end])
        else:
            for i, (s, e) in enumerate(intervals):
                if s > end:
                    intervals.insert(i, [start, end])
                    break
                elif e >= start:
                    intervals[i][0] = min(s, start)
                    intervals[i][1] = max(e, end)
                    break
            else:
                intervals.append([start, end])
        
    def mergeOverlappingIntervals(self) -> List[int[]]:
        if not self.intervals:
            return []
        merged = [self.intervals[0]]
        for i in range(1, len(self.intervals)):
            current = self.intervals[i]
            last = merged[-1]
            if current[0] <= last[1] + 1:
                merged[-1][1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged

    def removeInterval(self, start: int, end: int) -> None:
        intervals = self.intervals
        self.intervals = [interval for interval in intervals if interval[1] < start or interval[0] > end]

    def getIntervals(self) -> List[int[]]:
        return self.intervals
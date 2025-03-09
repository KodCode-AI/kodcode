from typing import List

class IntervalManager:
    def __init__(self):
        self.intervals = []
        
    def addInterval(self, start: int, end: int) -> None:
        # Ensure no duplicate intervals are added
        for interval in self.intervals:
            if interval[0] == start and interval[1] == end:
                return
        self.intervals.append([start, end])
        self.intervals = self.mergeOverlappingIntervals()
        
    def mergeOverlappingIntervals(self) -> List[int[]]:
        # Sort intervals based on start time
        self.intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in self.intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
    def removeInterval(self, start: int, end: int) -> None:
        self.intervals = [interval for interval in self.intervals if interval[0] != start or interval[1] != end]
        
    def getIntervals(self) -> List[int[]]:
        return self.intervals
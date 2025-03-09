from typing import List

class IntervalManager:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start: int, end: int) -> None:
        """
        Adds a new interval [start, end] to the collection if it does not already exist.
        """
        for s, e in self.intervals:
            if s <= start <= e or s <= end <= e or start <= s <= end or start <= e <= end:
                return
        self.intervals.append([start, end])
        self.intervals.sort(key=lambda x: x[0])

    def mergeOverlappingIntervals(self) -> List[int]:
        """
        Merges all overlapping intervals in the collection and returns the merged intervals.
        """
        merged = []
        for interval in self.intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        self.intervals = merged
        return self.intervals

    def removeInterval(self, start: int, end: int) -> None:
        """
        Removes the interval [start, end] from the collection if it exists.
        """
        self.intervals = [i for i in self.intervals if i[0] > end or i[1] < start]
        self.mergeOverlappingIntervals()

    def getIntervals(self) -> List[int]:
        """
        Returns the current collection of intervals.
        """
        return self.intervals
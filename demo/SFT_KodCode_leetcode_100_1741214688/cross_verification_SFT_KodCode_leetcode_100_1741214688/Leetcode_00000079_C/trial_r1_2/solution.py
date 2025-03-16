from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:
    def __init__(self, arr):
        self.index_map = defaultdict(list)
        for index, value in enumerate(arr):
            self.index_map[value].append(index)
    
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.index_map:
            return 0
        indexes = self.index_map[value]
        low = bisect_left(indexes, left)
        high = bisect_right(indexes, right)
        return high - low
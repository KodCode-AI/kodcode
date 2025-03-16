from collections import defaultdict
import bisect

class RangeFreqQuery:
    def __init__(self, arr):
        self.index_map = defaultdict(list)
        for index, value in enumerate(arr):
            self.index_map[value].append(integer)

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.index_map.get(value, [])
        if not indices:
            return 0
        left_pos = bisect.bisect_left(indices, left)
        right_pos = bisect.bisect_right(indices, right)
        return right_pos - left_pos
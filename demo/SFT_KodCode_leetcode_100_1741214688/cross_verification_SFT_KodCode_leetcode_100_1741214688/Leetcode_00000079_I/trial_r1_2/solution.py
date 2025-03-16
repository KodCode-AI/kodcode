import bisect
from collections import defaultdict

class RangeFreqQuery:
    def __init__(self, arr):
        self.value_indices = defaultdict(list)
        for index, value in enumerate(arr):
            self.value_indices[value].append(index)
    
    def query(self, left, right, value):
        if value not in self.value_indices:
            return 0
        indices = self.value_indices[value]
        left_rank = bisect.bisect_left(indices, left)
        right_rank = bisect.bisect_right(indices, right)
        return right_rank - left_rank
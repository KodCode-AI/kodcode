import bisect

class RangeFreqQuery:
    def __init__(self, arr):
        self.value_indices = {}
        for idx, value in enumerate(arr):
            if value not in self.value_indices:
                self.value_indices[value] = []
            self.value_indices[value].append(idx)
    
    def query(self, left, right, value):
        if value not in self.value_indices:
            return 0
        indices = self.value_indices[value]
        l = bisect.bisect_left(indices, left)
        r = bisect.bisect_right(indices, right)
        return r - l
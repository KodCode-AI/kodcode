from collections import defaultdict
import bisect

class RangeFreqQuery:
    def __init__(self, arr):
        """
        Initializes the class with the given array.
        """
        self.index_map = defaultdict(list)
        for index, value in enumerate(arr):
            self.index_map[value].append(index)
    
    def query(self, left: int, right: int, value: int) -> int:
        """
        Returns the frequency of the value in the subarray arr[left...right].
        """
        indexes = self.index_map.get(value, [])
        if left > right:
            return 0
        left_pos = bisect.bisect_left(indexes, left)
        right_pos = bisect.bisect_right(indexes, right)
        return right_pos - left_pos
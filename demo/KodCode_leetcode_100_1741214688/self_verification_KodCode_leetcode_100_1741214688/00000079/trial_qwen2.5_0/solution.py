from collections import defaultdict

class RangeFreqQuery:
    def __init__(self, arr):
        """
        Initializes the class with the given array.
        """
        self.index_map = defaultdict(list)
        for index, value in enumerate(arr):
            self.index_map[value].append(index)
    
    def query(self, left, right, value):
        """
        Returns the frequency of the value in the subarray arr[left...right].
        """
        if value not in self.index_map:
            return 0
        indices = self.index_map[value]
        left_idx = self._binary_search(indices, left)
        right_idx = self._binary_search(indices, right + 1) - 1
        return right_idx - left_idx + 1 if right_idx >= left_idx else 0
    
    def _binary_search(self, indices, target):
        left, right = 0, len(indices)
        while left < right:
            mid = (left + right) // 2
            if indices[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
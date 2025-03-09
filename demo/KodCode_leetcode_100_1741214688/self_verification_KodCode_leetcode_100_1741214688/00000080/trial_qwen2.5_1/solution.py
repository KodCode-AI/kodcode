import heapq
from typing import List

class KClosestPoints:
    def __init__(self, k: int):
        self.k = k
        self.min_heap = []

    def addPoint(self, x: int, y: int):
        distance = abs(x - tx) + abs(y - ty)
        heapq.heappush(self.min_heap, (distance, [x, y]))
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def getKClosestPoints(self) -> List[List[int]]:
        return [point for _, point in self.min_heap]
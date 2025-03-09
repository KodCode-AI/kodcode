import heapq
from typing import List

class KClosestPoints:
    def __init__(self, k: int):
        self.k = k
        self points_heap = []

    def addPoint(self, x: int, y: int, tx: int, ty: int):
        distance = abs(x - tx) + abs(y - ty)
        heapq.heappush(self.points_heap, (distance, x, y))
        if len(self.points_heap) > self.k:
            heapq.heappop(self.points_heap)

    def getKClosestPoints(self, tx: int, ty: int) -> List[List[int]]:
        return [[x, y] for _, x, y in heapq.nsmallest(self.k, self.points_heap)]
import heapq
from typing import List

class KClosestPoints:
    def __init__(self, k: int):
        self.k = k
        self.points = []

    def addPoint(self, x: int, y: int) -> None:
        point = (abs(x - tx) + abs(y - ty), x, y)
        heapq.heappush(self.points, point)

    def getKClosestPoints(self) -> List[List[int]]:
        k_closest = []
        for _ in range(self.k):
            _, x, y = heapq.heappop(self.points)
            k_closest.append([x, y])
        k_closest.sort()
        return k_closest
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == 0 or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) - len(self.large) > 1:
            item = heapq.heappop(self.small)
            heapq.heappush(self.large, -item)
        if len(self.large) > len(self.small):
            item = heapq.heappop(self.large)
            heapq.heappush(self.small, -item)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        large = self.large
        small = self.small
        heapq.heappush(small,-heapq.heappushpop(large,num))
        if len(small)>len(large):
            heapq.heappush(large,-heapq.heappop(small))

    def findMedian(self) -> float:
        large,small = self.large,self.small
        if len(large)>len(small):
            return large[0]
        return (large[0]-small[0])/2
        
        
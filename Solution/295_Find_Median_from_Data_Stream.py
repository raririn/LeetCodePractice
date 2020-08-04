class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, - heapq.heappop(self.minHeap))

        if (len(self.minHeap) < len(self.maxHeap)):
            heapq.heappush(self.minHeap, - heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

'''
Runtime: 220 ms, faster than 67.46% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 25.1 MB, less than 27.50% of Python3 online submissions for Find Median from Data Stream.
'''
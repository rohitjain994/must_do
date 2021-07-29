# https://leetcode.com/problems/find-mediawn-from-data-stream/

class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.pq1 = []
        self.pq2 = []
        

    def addNum(self, num: int) -> None:
        
            if len(self.pq1) == len(self.pq2):
                if not self.pq1 or (self.pq2 and self.pq2[0] > num):
                    heapq.heappush(self.pq1,-1*num)
                else:
                    heapq.heappush(self.pq1,-1*heapq.heappop(self.pq2))
                    heapq.heappush(self.pq2,num)
                    
            else:
                if self.pq1 and -1*self.pq1[0] < num:
                    heapq.heappush(self.pq2,num)
                else:
                    heapq.heappush(self.pq2,-1*heapq.heappop(self.pq1))
                    heapq.heappush(self.pq1,-1*num) 
        

    def findMedian(self) -> float:
        # print(self.pq1,self.pq2)
        if len(self.pq1) == len(self.pq2):
            return (-1*self.pq1[0] + self.pq2[0]) / 2
        return -1*self.pq1[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.pq=[]
        for i in nums:
            if len(self.pq)<k:
                heapq.heappush(self.pq,i)
            else:
                heapq.heappush(self.pq,i)
                heapq.heappop(self.pq)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pq)<self.k:
            heapq.heappush(self.pq,val)
        else:
            heapq.heappush(self.pq,val)
            heapq.heappop(self.pq)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
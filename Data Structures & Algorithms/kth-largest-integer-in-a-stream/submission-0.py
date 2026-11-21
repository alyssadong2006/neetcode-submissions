import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numList = nums
        heapq.heapify(self.numList)
        self.k = k

        # since k is constant
        # we can pop the smallest/root of the min heap to get largest k in the list
        # smaller numbers don't matter, since we'll never reference them even 
        # as new numbers come in
        while len(self.numList) > self.k:
            heapq.heappop(self.numList)
        
    def add(self, val: int) -> int:
        # add num to heap
        heapq.heappush(self.numList, val)

        # cut down the heap again 
        if len(self.numList) > self.k:
            heapq.heappop(self.numList)
        
        # the smallest number/root of the cut down heap is now the kth largest
        return self.numList[0]

        

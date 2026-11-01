import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        largestk = heapq.nlargest(k, counter, key = counter.get)

        return largestk

        
        

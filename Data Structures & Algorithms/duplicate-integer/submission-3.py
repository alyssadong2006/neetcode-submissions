class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenList = []
        for num in nums:
            if num not in seenList:
                seenList.append(num)
            else:
                return True
        return False
        
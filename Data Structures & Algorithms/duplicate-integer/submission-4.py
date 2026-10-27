class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) >= 2:
                return True
        return False
        
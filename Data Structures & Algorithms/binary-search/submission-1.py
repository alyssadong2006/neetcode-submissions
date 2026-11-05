class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
            
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return -1
        
        return -1
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        midIndex = len(nums)//2

        if nums == []:
            return -1
        elif nums[midIndex] == target:
            return midIndex
        elif nums[midIndex] > target:
            return self.search(nums[:midIndex], target)
        elif nums[midIndex] < target:
            return self.search(nums[midIndex + 1:], target)

        
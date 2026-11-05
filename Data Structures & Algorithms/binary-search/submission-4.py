from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # starts off with left = most left, right = most right
        left, right = 0, len(nums) - 1
        while left <= right:
            # middle index between left and right
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # move right limit to the left of mid
                right = mid - 1
            elif nums[mid] < target:
                # move left limit to the right of mid
                left = mid + 1
        # when left > right, means we've exhausted iterations
        return -1

        

        
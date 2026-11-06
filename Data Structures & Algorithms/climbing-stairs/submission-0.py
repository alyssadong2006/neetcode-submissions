class Solution:
    def climbStairs(self, n: int) -> int:
        countWays = 0
        while n > 0:
            if n - 2 >= 0:
                countWays += 2
                n = n - 2
            elif n - 1 >= 0:
                countWays += 1
                n = n - 1
        return countWays
        
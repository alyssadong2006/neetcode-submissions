class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1 # ways(1)
        prev1 = 2 # ways(2)

        current = 0

        # n step ways = (n - 1) ways + (n - 2) ways
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return current
        
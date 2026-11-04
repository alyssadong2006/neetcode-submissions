class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        for price in prices[1:]:
            if buy >= price:
                buy = price
                sell = price
                continue
            elif sell <= price:
                sell = price
                continue
        
        return sell - buy
        
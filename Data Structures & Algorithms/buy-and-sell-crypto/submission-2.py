class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0 

        for price in prices[1:]:
            if price < minPrice: 
                # update minPrice when new min is listed
                minPrice = price
            elif price - minPrice > maxProfit: 
                # if price is larger than minPrice, consider if that means
                # we can update maxProfit
                maxProfit = price - minPrice
        
        return maxProfit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestPrice = prices[0]
        for i in range(1, len(prices)):
            lowestPrice = min(lowestPrice, prices[i])
            profit = max(profit, prices[i] - lowestPrice)
        
        return profit
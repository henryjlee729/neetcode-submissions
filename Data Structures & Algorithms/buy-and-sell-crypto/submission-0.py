class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            lowest_price = min(lowest_price, prices[i])
            profit = max(profit, prices[i] - lowest_price)
        
        return profit
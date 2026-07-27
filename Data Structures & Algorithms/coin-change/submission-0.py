class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(0, len(dp)):
            dp[i] = float('inf')

        dp[0] = 0
        for currentAmount in range(1, amount + 1):
            for coin in coins:
                if coin <= currentAmount:
                    dp[currentAmount] = min(dp[currentAmount], dp[currentAmount - coin] + 1)

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]
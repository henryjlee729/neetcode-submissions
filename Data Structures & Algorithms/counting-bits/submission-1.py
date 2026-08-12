class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            numberWithoutLowestOne = i & (i - 1)
            dp[i] = dp[numberWithoutLowestOne] + 1

        return dp
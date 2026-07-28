class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        for i in range(0, len(dp)):
            dp[i] = False
        
        dp[0] = True
        for end in range(1, len(s) + 1):
            for start in range(0, end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
                    break

        return dp[len(s)]
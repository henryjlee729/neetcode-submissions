class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        for i in range(0, len(dp)):
            dp[i] = 1

        for current in range(1, len(nums)):
            for previous in range(0, current):
                if nums[previous] < nums[current]:
                    dp[current] = max(dp[current], dp[previous] + 1)
        
        answer = 1
        for val in dp:
            answer = max(answer, val)

        return answer
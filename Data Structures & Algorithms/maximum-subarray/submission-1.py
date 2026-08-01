class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        bestSum = nums[0]
        for index in range(1, len(nums)):
            currentNumber = nums[index]
            currentSum = max(currentNumber, currentSum + currentNumber)
            bestSum = max(bestSum, currentSum)

        return bestSum
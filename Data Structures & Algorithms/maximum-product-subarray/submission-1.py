class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        overallMax = nums[0]

        for i in range(1, len(nums)):
            currentNum = nums[i]
            previousMax = currentMax
            previousMin = currentMin

            currentMax = max(currentNum, currentNum * previousMax, currentNum * previousMin)
            currentMin = min(currentNum, currentNum * previousMax, currentNum * previousMin)
            overallMax = max(overallMax, currentMax)

        return overallMax
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for index in range(0, len(nums)):
            result = result ^ index
            result = result ^ nums[index]

        return result
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        start = 0
        combination = []
        sum = 0
        result = []
        self.backtrack(start, combination, sum, nums, target, result)

        return result

    def backtrack(self, start, combination, sum, nums, target, result):
        if sum == target:
            result.append(combination[:])
            return
        if sum > target:
            return

        for index in range(start, len(nums)):
            combination.append(nums[index])
            self.backtrack(index, combination, sum + nums[index], nums, target, result)
            combination.pop()
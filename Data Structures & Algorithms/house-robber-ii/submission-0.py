class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        reward1 = self.houseRobber(nums[0:len(nums) - 1])
        reward2 = self.houseRobber(nums[1:len(nums)])
        return max(reward1, reward2)

    def houseRobber(self, array):
        prevTwo = 0
        prevOne = 0
        for val in array:
            robCurrent = prevTwo + val
            skipCurrent = prevOne
            current = max(robCurrent, skipCurrent)

            prevTwo = prevOne
            prevOne = current

        return prevOne
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthestReach = 0
        for index in range(0, len(nums)):
            if index > furthestReach:
                return False

            furthestReach = max(furthestReach, index + nums[index])

        return True
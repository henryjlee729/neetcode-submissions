class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in myMap:
                return [myMap[nums[i]], i]
            else:
                myMap[difference] = i
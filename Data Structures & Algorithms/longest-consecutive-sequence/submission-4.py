class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for num in mySet:
            if num - 1 not in mySet:
                count = 1
                current = num

                while current + 1 in mySet:
                    count += 1
                    current += 1
            
                longest = max(longest, count)
        
        return longest
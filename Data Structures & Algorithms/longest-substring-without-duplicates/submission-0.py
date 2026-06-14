class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        largest = 0
        left = 0
        for c in s:
            while c in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(c)
            largest = max(largest, len(substring))

        return largest
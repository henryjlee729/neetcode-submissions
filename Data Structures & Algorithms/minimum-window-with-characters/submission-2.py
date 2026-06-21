from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        bestLeft = 0
        bestRight = 0
        bestLength = float("inf")

        formed = 0
        required = len(set(t))

        sCounter = Counter()
        tCounter = Counter(t)
        for right in range(len(s)):
            rC = s[right]
            sCounter[rC] += 1
            if rC in tCounter and sCounter[rC] == tCounter[rC]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < bestLength:
                    bestLength = right - left + 1
                    bestLeft = left
                    bestRight = right
                
                lC = s[left]
                sCounter[lC] -= 1
                if lC in tCounter and sCounter[lC] < tCounter[lC]:
                    formed -= 1

                left += 1
        
        if bestLength == float("inf"):
            return ""
        
        return s[bestLeft : bestRight + 1]
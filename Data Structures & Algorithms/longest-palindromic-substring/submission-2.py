class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestStart = 0
        bestLength = 1
        for center in range(0, len(s)):
            left = center
            right = center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLength = right - left + 1

                if currentLength > bestLength:
                    bestStart = left
                    bestLength = currentLength

                left = left - 1
                right = right + 1

            left = center
            right = center + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLength = right - left + 1

                if currentLength > bestLength:
                    bestStart = left
                    bestLength = currentLength

                left = left - 1
                right = right + 1

        return s[bestStart:bestStart + bestLength]
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0

        waysTwoBack = 1
        waysOneBack = 1
        for i in range(1, len(s)):
            currentWays = 0
            if s[i] != "0":
                currentWays += waysOneBack
            
            twoDigitNumber = s[i - 1] + s[i]
            if int(twoDigitNumber) >= 10 and int(twoDigitNumber) <= 26:
                currentWays += waysTwoBack

            waysTwoBack = waysOneBack
            waysOneBack = currentWays

        return waysOneBack
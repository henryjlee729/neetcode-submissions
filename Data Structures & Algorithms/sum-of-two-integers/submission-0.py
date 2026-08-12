class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            sumWithoutCarry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sumWithoutCarry
            b = carry

        return a if a < 0x80000000 else a - 0x100000000
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            S = num1 - k * num2
            if S <= 0:
                continue
            if S.bit_count() <= k <= S:
                return k
        return -1

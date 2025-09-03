class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        INF = n + 2
        bMin1 = [INF] * (n + 2)
        bMin2 = [INF] * (n + 2) 
        for a, b in conflictingPairs:
            a, b = min(a, b), max(a, b)
            if b < bMin1[a]:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif b < bMin2[a]:
                bMin2[a] = b
        res = 0
        delCount = [0] * (n + 2)
        ib1 = n + 1
        b2 = INF
        for i in range(n, 0, -1):

            if bMin1[i] < bMin1[ib1]:
                b2 = min(b2, bMin1[ib1])
                ib1 = i
            else:
                b2 = min(b2, bMin1[i])
            maxRight = min(bMin1[ib1], n + 1)
            res += maxRight - i
            delInc = min(min(b2, bMin2[ib1]), n + 1) - maxRight
            if delInc > 0:
                delCount[ib1] += delInc
        return res + max(delCount)

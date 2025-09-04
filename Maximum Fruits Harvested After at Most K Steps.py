import itertools

class Solution:
    def maxTotalFruits(self, fruits, startPos: int, k: int) -> int:
        ans = 0
        maxRight = max(startPos, fruits[-1][0])
        amounts = [0] * (maxRight + 1)
        for position, amount in fruits:
            amounts[position] = amount
        prefix = list(itertools.accumulate(amounts, initial=0))

        def getFruits(leftSteps, rightSteps):
            l = max(0, startPos - leftSteps)
            r = min(maxRight, startPos + rightSteps)
            return prefix[r + 1] - prefix[l]
        

        for rightSteps in range(min(maxRight - startPos, k) + 1):
            leftSteps = max(0, k - 2 * rightSteps)
            ans = max(ans, getFruits(leftSteps, rightSteps))
        

        for leftSteps in range(min(startPos, k) + 1):
            rightSteps = max(0, k - 2 * leftSteps)
            ans = max(ans, getFruits(leftSteps, rightSteps))
        
        return ans

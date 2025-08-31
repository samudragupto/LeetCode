from math import factorial

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        k -= 1
        result = []
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
        for i in range(n, 0, -1):
            f = factorials[i-1]
            index = k // f
            result.append(str(numbers.pop(index)))
            k %= f
        return ''.join(result)

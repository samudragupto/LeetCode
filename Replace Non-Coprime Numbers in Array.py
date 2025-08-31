import math

class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        
        for num in nums:
            while stack and math.gcd(stack[-1], num) > 1:
                top = stack.pop()
                num = (top * num) // math.gcd(top, num)
            stack.append(num)
        
        return stack

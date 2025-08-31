class Solution:
    def calculate(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1
        
        i = 0
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1
                result += sign * number
                continue
            
            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            
            i += 1
        
        return result

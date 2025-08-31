from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        res = []
        visited = set([s])
        queue = deque([s])
        found = False
        
        while queue:
            string = queue.popleft()
            if is_valid(string):
                res.append(string)
                found = True
            if found:
                continue
            for i in range(len(string)):
                if string[i] not in '()':
                    continue
                next_str = string[:i] + string[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        
        return res if res else [""]

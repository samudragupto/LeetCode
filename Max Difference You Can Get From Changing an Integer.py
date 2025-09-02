class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        def replace_num(s, x, y):
            res = []
            for c in s:
                if c == x:
                    res.append(y)
                else:
                    res.append(c)
            res_str = ''.join(res)
            if res_str[0] == '0':
                return None
            return int(res_str)
        
        max_num = -1
        min_num = 10**10
        
        x_max = None
        for c in num_str:
            if c != '9':
                x_max = c
                break
        if x_max is None:
            max_num = int(num_str)
        else:
            max_num = int(num_str.replace(x_max, '9'))
        
        first = num_str[0]
        if first != '1':
            min_num = int(num_str.replace(first, '1'))
        else:
            found = False
            for c in num_str[1:]:
                if c != '0' and c != '1':
                    min_num = int(num_str.replace(c, '0'))
                    found = True
                    break
            if not found:
                min_num = int(num_str)
        
        return max_num - min_num

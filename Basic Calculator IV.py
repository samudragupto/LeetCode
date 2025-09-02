from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        mapping = dict(zip(evalvars, evalints))

        def tokenize(s):
            return s.replace('(', ' ( ').replace(')', ' ) ').split()

        def add(poly1, poly2):
            res = defaultdict(int)
            for k, v in poly1.items():
                res[k] += v
            for k, v in poly2.items():
                res[k] += v
            return {k: v for k, v in res.items() if v != 0}

        def multiply(poly1, poly2):
            res = defaultdict(int)
            for k1, v1 in poly1.items():
                for k2, v2 in poly2.items():
                    vars = tuple(sorted(k1 + k2))
                    res[vars] += v1 * v2
            return {k: v for k, v in res.items() if v != 0}

        def negate(poly):
            return {k: -v for k, v in poly.items()}

        def parse(tokens):
            def helper():
                stack = []
                op = '+'

                def calc_op(num):
                    nonlocal op
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(negate(num))
                    elif op == '*':
                        prev = stack.pop()
                        stack.append(multiply(prev, num))

                while tokens:
                    token = tokens.pop(0)
                    if token == '(':
                        num = helper()
                        calc_op(num)
                    elif token == ')':
                        break
                    elif token in ('+', '-', '*'):
                        op = token
                    else:
                        if token.isdigit():
                            num = {(): int(token)}
                        else:
                            if token in mapping:
                                num = {(): mapping[token]}
                            else:
                                num = {(token,): 1}
                        calc_op(num)
                result = defaultdict(int)
                for item in stack:
                    for k, v in item.items():
                        result[k] += v
                return {k: v for k, v in result.items() if v != 0}
            return helper()

        tokens = tokenize(expression)
        poly = parse(tokens)

        def key_func(k):
            return (-len(k), k)

        res = []
        for k in sorted(poly.keys(), key=key_func):
            v = poly[k]
            if k == ():
                res.append(str(v))
            else:
                res.append(str(v) + '*' + '*'.join(k))
        return res

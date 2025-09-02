class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def merge(left, op, right):
            lv, lc0, lc1 = left
            rv, rc0, rc1 = right
            results = []
            if op == '&':
                for lval, lcost in [(lv, (lc0, lc1)),]:
                    for rval, rcost in [(rv, (rc0, rc1)),]:
                        for ltarget in (0, 1):
                            for rtarget in (0, 1):
                                val = ltarget & rtarget
                                cost = (lc0 if ltarget == 0 else lc1) - (lc0 if lv == 0 else lc1) + \
                                       (rc0 if rtarget == 0 else rc1) - (rc0 if rv == 0 else rc1)
                                cost = (lc0 if ltarget == 0 else lc1) + (rc0 if rtarget == 0 else rc1)
                                results.append((val, cost))
            else:
                for ltarget in (0, 1):
                    for rtarget in (0, 1):
                        val = ltarget | rtarget
                        cost = (lc0 if ltarget == 0 else lc1) + (rc0 if rtarget == 0 else rc1)
                        results.append((val, cost))
            flipped_op = '|' if op == '&' else '&'
            if flipped_op == '&':
                for ltarget in (0, 1):
                    for rtarget in (0, 1):
                        val = ltarget & rtarget
                        cost = 1 + (lc0 if ltarget == 0 else lc1) + (rc0 if rtarget == 0 else rc1)
                        results.append((val, cost))
            else:
                for ltarget in (0, 1):
                    for rtarget in (0, 1):
                        val = ltarget | rtarget
                        cost = 1 + (lc0 if ltarget == 0 else lc1) + (rc0 if rtarget == 0 else rc1)
                        results.append((val, cost))

            min_cost0 = min((cost for val, cost in results if val == 0), default=float('inf'))
            min_cost1 = min((cost for val, cost in results if val == 1), default=float('inf'))

            val = lv & rv if op == '&' else lv | rv
            return val, min_cost0, min_cost1

        stack_val = []
        stack_op = []
        i = 0
        n = len(expression)

        while i < n:
            c = expression[i]
            if c == '0':
                stack_val.append((0, 0, 1))
                i += 1
            elif c == '1':
                stack_val.append((1, 1, 0))
                i += 1
            elif c == '(':
                stack_op.append(c)
                i += 1
            elif c == ')':
                while stack_op and stack_op[-1] != '(':
                    op = stack_op.pop()
                    right = stack_val.pop()
                    left = stack_val.pop()
                    stack_val.append(merge(left, op, right))
                stack_op.pop()
                i += 1
            else:
                while stack_op and stack_op[-1] != '(' and len(stack_val) >= 2:
                    op = stack_op.pop()
                    right = stack_val.pop()
                    left = stack_val.pop()
                    stack_val.append(merge(left, op, right))
                stack_op.append(c)
                i += 1

        while stack_op:
            op = stack_op.pop()
            right = stack_val.pop()
            left = stack_val.pop()
            stack_val.append(merge(left, op, right))

        val, cost0, cost1 = stack_val[-1]
        return cost1 if val == 0 else cost0

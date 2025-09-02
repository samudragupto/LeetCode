class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        rows = {}
        cols = {}
        diag = {}
        anti = {}
        on = set()
        for x, y in lamps:
            if (x, y) in on: continue
            on.add((x, y))
            rows[x] = rows.get(x, 0) + 1
            cols[y] = cols.get(y, 0) + 1
            d = x - y
            diag[d] = diag.get(d, 0) + 1
            a = x + y
            anti[a] = anti.get(a, 0) + 1

        ans = []
        for x, y in queries:
            if rows.get(x, 0) or cols.get(y, 0) or diag.get(x - y, 0) or anti.get(x + y, 0):
                ans.append(1)
            else:
                ans.append(0)
            for i in (x-1, x, x+1):
                for j in (y-1, y, y+1):
                    if (i, j) in on:
                        on.remove((i, j))
                        rows[i] -= 1
                        if rows[i] == 0: del rows[i]
                        cols[j] -= 1
                        if cols[j] == 0: del cols[j]
                        d2 = i - j
                        diag[d2] -= 1
                        if diag[d2] == 0: del diag[d2]
                        a2 = i + j
                        anti[a2] -= 1
                        if anti[a2] == 0: del anti[a2]
        return ans

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        xs = sorted(set(p[0] for p in points))
        ys = sorted(set(p[1] for p in points))
        x_idx = {x: i+1 for i, x in enumerate(xs)}
        y_idx = {y: i+1 for i, y in enumerate(ys)}
        size_x, size_y = len(xs), len(ys)

        grid = [[0] * (size_y + 1) for _ in range(size_x + 1)]

        for x, y in points:
            grid[x_idx[x]][y_idx[y]] = 1

        for i in range(1, size_x + 1):
            row_sum = 0
            for j in range(1, size_y + 1):
                row_sum += grid[i][j]
                grid[i][j] = grid[i - 1][j] + row_sum

        def query(x1, y1, x2, y2):
            return grid[x2][y2] - grid[x1 - 1][y2] - grid[x2][y1 - 1] + grid[x1 - 1][y1 - 1]

        ans = 0
        px_idx = points
        for i in range(n):
            xA, yA = px_idx[i]
            xiA, yiA = x_idx[xA], y_idx[yA]
            for j in range(n):
                if i == j:
                    continue
                xB, yB = px_idx[j]
                if xA > xB or yA < yB:
                    continue
                xiB, yiB = x_idx[xB], y_idx[yB]
                x1, x2 = xiA, xiB
                y1, y2 = yiB, yiA  # yB ≤ yA guaranteed
                ans += 1 if query(x1, y1, x2, y2) == 2 else 0

        return ans

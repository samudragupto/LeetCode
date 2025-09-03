class Solution:
    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])
        next_digit = {1: 2, 2: 0, 0: 2}
        from functools import cache
        
        def within_bounds(i, j):
            return 0 <= i < m and 0 <= j < n
        
        @cache
        def f(i, j, di, dj, turned):
            result = 1
            successor = next_digit[grid[i][j]]

            if within_bounds(i + di, j + dj) and grid[i + di][j + dj] == successor:
                result = 1 + f(i + di, j + dj, di, dj, turned)

            if not turned:
                new_di, new_dj = dj, -di
                if within_bounds(i + new_di, j + new_dj) and grid[i + new_di][j + new_dj] == successor:
                    result = max(result, 1 + f(i + new_di, j + new_dj, new_di, new_dj, True))
            
            return result
        
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        result = max(result, f(i, j, di, dj, False))
        
        return result

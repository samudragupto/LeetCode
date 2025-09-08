class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        n = len(grid)
        diagonals = defaultdict(list)
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
        for d, vals in diagonals.items():
            if d >= 0:
                vals.sort(reverse=True)
            else:
                vals.sort()
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)
        return grid

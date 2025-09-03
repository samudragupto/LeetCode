class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[(i//3)*3 + (j//3)].add(c)
                else:
                    empties.append((i, j))

        def candidates(i, j):
            return set(str(x) for x in range(1, 10)) - rows[i] - cols[j] - boxes[(i//3)*3 + (j//3)]

        def dfs(idx):
            if idx == len(empties):
                return True

            min_idx, min_cands = idx, candidates(*empties[idx])
            for k in range(idx+1, len(empties)):
                cand = candidates(*empties[k])
                if len(cand) < len(min_cands):
                    min_idx, min_cands = k, cand
                if len(min_cands) == 1:
                    break
            empties[idx], empties[min_idx] = empties[min_idx], empties[idx]
            i, j = empties[idx]
            for c in min_cands:
                board[i][j] = c
                rows[i].add(c)
                cols[j].add(c)
                boxes[(i//3)*3 + (j//3)].add(c)
                if dfs(idx+1):
                    return True
                rows[i].remove(c)
                cols[j].remove(c)
                boxes[(i//3)*3 + (j//3)].remove(c)
                board[i][j] = '.'
            return False

        dfs(0)

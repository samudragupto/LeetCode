class Solution:
    def totalNQueens(self, n):
        def backtrack(row=0, cols=0, diags=0, anti_diags=0):
            if row == n:
                return 1
            count = 0
            available_positions = ((1 << n) - 1) & ~(cols | diags | anti_diags)
            while available_positions:
                position = available_positions & (-available_positions)
                available_positions &= available_positions - 1
                count += backtrack(row + 1, 
                                   cols | position, 
                                   (diags | position) << 1, 
                                   (anti_diags | position) >> 1)
            return count
        
        return backtrack()

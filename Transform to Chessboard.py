class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)
        
        # Check rows pattern
        first_row = board[0]
        row_sum = sum(first_row)
        row_pattern_count = 0
        for row in board:
            if row != first_row and row != [1 - x for x in first_row]:
                return -1
            if row == first_row:
                row_pattern_count += 1
        
        # Check columns pattern
        first_col = [board[i][0] for i in range(n)]
        col_sum = sum(first_col)
        col_pattern_count = 0
        for j in range(n):
            col = [board[i][j] for i in range(n)]
            if col != first_col and col != [1 - x for x in first_col]:
                return -1
            if col == first_col:
                col_pattern_count += 1
        
        def moves_to_arrange(line, count):
            ones = sum(line)
            length = len(line)
            
            if not (length // 2 <= ones <= (length + 1) // 2):
                return -1
            
            def count_swaps(target_pattern):
                swaps = 0
                for i in range(length):
                    if line[i] != target_pattern[i]:
                        swaps += 1
                return swaps // 2

            pattern1 = [i % 2 for i in range(length)]
            pattern2 = [1 - i % 2 for i in range(length)]

            res = float('inf')
            if length % 2 == 0:
                res = min(count_swaps(pattern1), count_swaps(pattern2))
            else:
                if sum(pattern1) == ones:
                    res = min(res, count_swaps(pattern1))
                if sum(pattern2) == ones:
                    res = min(res, count_swaps(pattern2))
            
            if res == float('inf'):
                return -1
            else:
                return res
        
        row_moves = moves_to_arrange(first_row, row_pattern_count)
        if row_moves == -1:
            return -1
        col_moves = moves_to_arrange(first_col, col_pattern_count)
        if col_moves == -1:
            return -1
        
        return row_moves + col_moves

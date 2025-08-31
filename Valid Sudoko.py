class Solution:
    def isValidSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = 1 << (int(board[i][j]) - 1)
                box_index = (i // 3) * 3 + (j // 3)
                
                if (rows[i] & num) or (cols[j] & num) or (boxes[box_index] & num):
                    return False
                
                rows[i] |= num
                cols[j] |= num
                boxes[box_index] |= num
                
        return True

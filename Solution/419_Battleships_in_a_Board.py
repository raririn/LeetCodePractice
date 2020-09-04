class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] == 'X':
                    if (c == 0 or board[r][c-1] != 'X') and (r == 0 or board[r-1][c] != 'X'):
                        count += 1
        
        return count


'''
Runtime: 72 ms, faster than 87.84% of Python3 online submissions for Battleships in a Board.
Memory Usage: 14.1 MB, less than 49.97% of Python3 online submissions for Battleships in a Board.
'''
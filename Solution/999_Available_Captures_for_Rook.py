class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = (i, j)
                    break
        
        count = 0

        for i in range(rook[0], -1, -1):
            if board[i][rook[1]] == 'B':
                break
            elif board[i][rook[1]] == 'p':
                count += 1
                break
        
        for i in range(rook[0], 8):
            if board[i][rook[1]] == 'B':
                break
            elif board[i][rook[1]] == 'p':
                count += 1
                break

        for j in range(rook[1], -1, -1):
            if board[rook[0]][j] == 'B':
                break
            elif board[rook[0]][j] == 'p':
                count += 1
                break

        for j in range(rook[1], 8):
            if board[rook[0]][j] == 'B':
                break
            elif board[rook[0]][j] == 'p':
                count += 1
                break

        return count                        

'''
Runtime: 28 ms, faster than 88.85% of Python3 online submissions for Available Captures for Rook.
Memory Usage: 13.8 MB, less than 74.77% of Python3 online submissions for Available Captures for Rook.
'''
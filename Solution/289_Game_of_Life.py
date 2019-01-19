class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # Not solved, did not understand the problem
        l = len(board)
        w = len(board[0])
        neighboard = [[None]*w]*l
        for i in range(l):
            for j in range(w):
                neighbor = 0
                if i > 0:
                    if board[i-1][j]:
                        neighbor += 1
                    if j > 0:
                        if board[i-1][j-1]:
                            neighbor += 1
                if j > 0:
                    if board[i][j-1]:
                        neighbor += 1
                    if i < l - 1:
                        if board[i+1][j-1]:
                            neighbor += 1
                if i < l - 1:
                    if board[i+1][j]:
                        neighbor += 1
                    if j < w - 1:
                        if board[i+1][j+1]:
                            neighbor += 1                
                if j < w - 1:
                    if board[i][j+1]:
                        neighbor += 1
                    if i > 0:
                        if board[i-1][j+1]:
                            neighbor += 1
                neighboard[i][j] = neighbor
        for i in range(l):
            for j in range(w):
                if board[i][j]:
                    if not neighboard[i][j] in [2,3]:
                        board[i][j] = 0
                else:
                    if neighboard[i][j] == 3:
                        board[i][j] = 1
        return
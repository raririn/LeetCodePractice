class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        def checkList(L: List[str]):
            c = Counter(L)
            for k, v in c.items():
                if k != '.' and v > 1:
                    return False
            return True
        def checkCol(board: List[List[str]]):
            L = []
            for col in range(0, 9):
                L.append([board[i][col] for i in range(len(board))])
            return L
        def checkRow(board: List[List[str]]):
            L = []
            for row in range(0, 9):
                L.append(board[row])
            return L
        def checkblock(board: List[List[str]]):
            L = []
            for i in range(0, 3):
                for j in range (0, 3):
                    L.append([board[3*j+0][k] for k in range(3*i, 3*i+3)] + \
                    [board[3*j+1][k] for k in range(3*i, 3*i+3)] + \
                    [board[3*j+2][k] for k in range(3*i, 3*i+3)])
            return L

        L =  checkRow(board) + checkCol(board) + checkblock(board)
        for i in L:
            if not checkList(i):
                print(i)
                return False
        return True


'''
Runtime: 140 ms, faster than 15.17% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14 MB, less than 11.19% of Python3 online submissions for Valid Sudoku.
'''
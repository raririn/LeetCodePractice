class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.L = len(board)
        self.W = len(board[0])
        self.lenw = len(word)
        self.word = word
        
        for i in range(self.L):
            for j in range(self.W):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0) or self.lenw == 1:
                        return True
        return False

    def dfs(self, x, y, ptr):
        if ptr == self.lenw:
            return True
        if not self.board[x][y] == self.word[ptr]:
            return False
        tmp = self.board[x][y]
        self.board[x][y] = '#'
        for neighbor in self.BFS_component(x, y):
            if self.dfs(neighbor[0], neighbor[1], ptr+1):
                return True
        self.board[x][y] = tmp
        return False


    def BFS_component(self, x, y):
        ret = []
        if x > 0:
            ret.append((x-1, y))
        if y > 0:
            ret.append((x, y-1))
        if x < self.L-1:
            ret.append((x+1, y))
        if y < self.W-1:
            ret.append((x, y+1))
        return ret

'''
Runtime: 396 ms, faster than 51.12% of Python3 online submissions for Word Search.
Memory Usage: 14.9 MB, less than 25.53% of Python3 online submissions for Word Search.
'''
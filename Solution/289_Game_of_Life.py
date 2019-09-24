class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.l = len(board)
        self.w = len(board[0])
        status = [[0] * self.w for _ in range(self.l)]
        for i in range(self.l):
            for j in range(self.w):
                status[i][j] = self.statusUpdate(board[i][j], self.countLivingNeighbor([i, j]))
                #print("prev: ", i, j ,board[i][j], " count: ", self.countLivingNeighbor([i, j]), " after:", status[i][j])
        for i in range(self.l):
            for j in range(self.w):
                board[i][j] = status[i][j]
    
    @staticmethod
    def statusUpdate(prev: int, neighbors: int) -> int:
        if prev and (neighbors < 2 or neighbors > 3):
            return 0
        if (not prev) and (neighbors == 3):
            return 1
        return prev

    def countLivingNeighbor(self, cell: List[int]) -> int:
        countList = [0] * 8
        if cell[0] >= 1: #Left
            countList[0] = self.board[cell[0]-1][cell[1]]
            if cell[1] >= 1:
                countList[4] = self.board[cell[0]-1][cell[1]-1] # Leftup
            if cell[1] <= self.w - 2:
                countList[5] = self.board[cell[0]-1][cell[1]+1] # LeftDown

        if cell[0] <= self.l - 2:    # Right
            countList[1] = self.board[cell[0]+1][cell[1]]
            if cell[1] >= 1:
                countList[6] = self.board[cell[0]+1][cell[1]-1] # Rightup
            if cell[1] <= self.w - 2:
                countList[7] = self.board[cell[0]+1][cell[1]+1] # Rightdown

        if cell[1] >= 1: # Up
            countList[2] = self.board[cell[0]][cell[1]-1]
        
        if cell[1] <= self.w - 2:    # Down
            countList[3] = self.board[cell[0]][cell[1]+1]
        return sum(countList)

'''
Runtime: 44 ms, faster than 27.25% of Python3 online submissions for Game of Life.
Memory Usage: 13.5 MB, less than 10.00% of Python3 online submissions for Game of Life.
'''
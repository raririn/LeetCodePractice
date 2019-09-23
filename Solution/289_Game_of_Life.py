class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.l = len(board)
        self.w = len(board[0])
        status = [[0] * self.w] * self.l
        for i in range(self.l):
            for j in range(self.w):
    
    def statusUpdate(prev: int, neighbors: int) -> int:
        if prev and (neighbors < 2 or neighbors == 4):
            return 0
        if (not prev) and (neighbors == 3):
            return 1
        return prev

    def countLivingNeighbor(self, cell: List[int]) -> int:
        count = 0
        if cell[0] >= 1 and self.board[cell[0]-1][cell[1]]:
            count = count + 1
        if cell[0] <= self.l - 2 and self.board[cell[0]+1][cell[1]]:
            count = count + 1
        if cell[1] >= 1 and self.board[cell[0]][cell[1]-1]:
            count = count + 1
        if cell[1] <= self.w - 2 and self.board[cell[0]][cell[1]+1]:
            count = count + 1
        return count
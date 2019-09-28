class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.l = len(grid)
        self.w = len(grid[0])
        ret = 0
        for i in range(self.l):
            for j in range(self.w):
                ret = ret + self.getPointPerimeter(i, j)
        return ret

    def getPointPerimeter(self, x: int, y: int) -> int:
        if not self.grid[x][y]:
            return 0
        p = 0

        if y == self.w - 1:
            p = p + 1
        else:
            p = p + (self.grid[x][y+1] == 0)

        if x == 0:
            p = p + 1
        else:
            p = p + (self.grid[x-1][y] == 0)

        if y == 0:
            p = p + 1
        else:
            p = p + (self.grid[x][y-1] == 0)

        if x == self.l - 1:
            p = p + 1
        else:
            p = p + (self.grid[x+1][y] == 0)
            
        return p

'''
Runtime: 648 ms, faster than 37.12% of Python3 online submissions for Island Perimeter.
Memory Usage: 14.1 MB, less than 25.00% of Python3 online submissions for Island Perimeter.
'''
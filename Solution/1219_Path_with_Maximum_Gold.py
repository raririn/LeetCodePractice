class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        self.dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for r, i in enumerate(grid):
            for c, j in enumerate(i):
                if grid[r][c]:
                    self.visited = set()
                    self.dfs(r, c, grid[r][c])
        return max(c for r in self.dp for c in r)


    def dfs(self, r, c, val):
        self.visited.add((r, c))
        self.dp[r][c] = max(self.dp[r][c], val)
        for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= x < self.R and 0 <= y < self.C and self.grid[x][y] and (not ((x, y) in self.visited)):
                self.dfs(x, y, val+self.grid[x][y])
        self.visited.discard((r, c))

'''
Runtime: 1724 ms, faster than 48.38% of Python3 online submissions for Path with Maximum Gold.
Memory Usage: 13.8 MB, less than 85.09% of Python3 online submissions for Path with Maximum Gold.
'''
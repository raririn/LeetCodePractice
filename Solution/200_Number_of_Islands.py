class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.visited = set()
        self.ret = 0
        self.R = len(grid)
        self.C = len(grid[0])

        def inGrid(t):
            r, c = t
            if r < 0 or r >= self.R:
                return False
            if c < 0 or c >= self.C:
                return False
            if grid[r][c] == '0':
                return False
            return True

        def getNeighbors(t):
            r, c = t
            return list(filter(inGrid, [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]))

        def dfs(t):
            if t in self.visited:
                return
            #print(t, self.visited)
            self.ret += 1
            stack = [t]
            while stack:
                cur = stack.pop()
                for i in getNeighbors(cur):
                    if not i in self.visited:
                        self.visited.add(i)
                        stack.append(i)
            return
        
        for r in range(self.R):
            for c in range(self.C):
                if inGrid((r, c)):
                    dfs((r, c))

        return self.ret


'''
Runtime: 196 ms, faster than 33.79% of Python3 online submissions for Number of Islands.
Memory Usage: 18.7 MB, less than 11.64% of Python3 online submissions for Number of Islands.
'''
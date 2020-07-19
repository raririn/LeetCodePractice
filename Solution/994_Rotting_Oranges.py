class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    q.append((r, c))
        

        if not q:
            for i in grid:
                if 1 in i:
                    return -1
            return 0
        
        ret = 0
        R = len(grid)
        C = len(grid[0])

        while q:
            for _ in range(len(q)):
                r, c = q.pop()
                
                if r > 0 and grid[r-1][c] == 1:
                    q.appendleft((r-1, c))
                    grid[r-1][c] = 2
                if r+1 < R and grid[r+1][c] == 1:
                    q.appendleft((r+1, c))
                    grid[r+1][c] = 2
                if c > 0 and grid[r][c-1] == 1:
                    q.appendleft((r, c-1))
                    grid[r][c-1] = 2
                if c+1 < C and grid[r][c+1] == 1:
                    q.appendleft((r, c+1))
                    grid[r][c+1] = 2
            if q:
                ret += 1


        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    return -1

        return ret


'''
Runtime: 56 ms, faster than 63.55% of Python3 online submissions for Rotting Oranges.
Memory Usage: 13.8 MB, less than 62.08% of Python3 online submissions for Rotting Oranges.
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        from operator import add
        flattened = reduce(add, grid)
        m, n = len(grid), len(grid[0])
        k = k % (m*n)  

        flattened = flattened[-k:] + flattened[:-k]
        for i in range(m):
            for j in range(n):
                grid[i][j] = flattened[i*n + j]
        
        return grid

'''
Runtime: 180 ms, faster than 64.61% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.3 MB, less than 9.85% of Python3 online submissions for Shift 2D Grid.
'''
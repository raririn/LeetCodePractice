class Solution:
    '''
    Really confusing problem...
    '''
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ret = 0
        for i in range(n):
            maxrow = 0
            maxcol = 0
            for j in range(n):
                if grid[i][j]:
                    ret += 1
                maxrow = max(maxrow, grid[i][j])
                maxcol = max(maxcol, grid[j][i])
            ret += (maxrow + maxcol)
        return ret

'''
Runtime: 96 ms, faster than 18.84% of Python3 online submissions for Projection Area of 3D Shapes.
Memory Usage: 14.1 MB, less than 12.50% of Python3 online submissions for Projection Area of 3D Shapes.
'''
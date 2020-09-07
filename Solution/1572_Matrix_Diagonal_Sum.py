class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        D = len(mat)

        ret = 0
        for x in range(D):
            ret += mat[x][x]
            ret += mat[D-x-1][x]
        
        if D & 1 == 1:
            ret -= mat[D//2][D//2]
        
        return ret

'''
Runtime: 108 ms, faster than 66.67% of Python3 online submissions for Matrix Diagonal Sum.
Memory Usage: 14 MB, less than 33.33% of Python3 online submissions for Matrix Diagonal Sum.
'''
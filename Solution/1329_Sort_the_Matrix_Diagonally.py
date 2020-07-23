class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])

        for r in range(R):
            c_range = range(min(R-r, C))
            diagon = sorted(mat[r+c][c] for c in c_range)
            for c in c_range:
                mat[r+c][c] = diagon[c]
        
        for c in range(1, C):
            r_range = range(min(C-c, R))
            diagon = sorted(mat[r][r+c] for r in r_range)
            for r in r_range:
                mat[r][r+c] = diagon[r]
        
        return mat

'''
Runtime: 152 ms, faster than 17.16% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14 MB, less than 58.85% of Python3 online submissions for Sort the Matrix Diagonally.
'''
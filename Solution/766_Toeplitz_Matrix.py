class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R, C = len(matrix), len(matrix[0])
        for j in range(C):
            t = matrix[0][j]
            for i in range(R):
                if j+i > C-1:
                    break
                if matrix[i][j+i] != t:
                    return False
        
        for i in range(R):
            t = matrix[i][0]
            for j in range(C):
                if i+j > R-1:
                    break
                if matrix[i+j][j] != t:
                    return False

        return True

'''
Runtime: 92 ms, faster than 70.17% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.9 MB, less than 44.89% of Python3 online submissions for Toeplitz Matrix.
'''
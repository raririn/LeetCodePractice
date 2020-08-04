class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        flag = False
        
        for r in range(R):
            if matrix[r][0] == 0:
                flag = True
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for c in range(C):
                matrix[0][c] = 0
        
        if flag:
            for r in range(R):
                matrix[r][0] = 0
        
        return 

'''
Runtime: 140 ms, faster than 71.31% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.3 MB, less than 28.52% of Python3 online submissions for Set Matrix Zeroes.
'''
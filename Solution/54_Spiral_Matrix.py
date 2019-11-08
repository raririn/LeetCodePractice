class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while len(matrix) > 1 and len(matrix[0]) > 1:
            # Remove the first row
            for i in range(len(matrix[0])):
                ret.append(matrix[0][i])
            matrix = matrix[1:]

            # Remove the last column
            for i in range(len(matrix)):
                ret.append(matrix[i][-1])
                matrix[i] = matrix[i][:-1]
            
            # Remove the last row
            for i in range(len(matrix[0])-1, -1, -1):
                ret.append(matrix[-1][i])
            matrix = matrix[:-1]

            # Remove the first column
            for i in range(len(matrix)-1, -1, -1):
                ret.append(matrix[i][0])
                matrix[i] = matrix[i][1:] 
        for i in matrix:
            for j in i:
                ret.append(j)
        return ret           

'''
Runtime: 24 ms, faster than 99.84% of Python3 online submissions for Spiral Matrix.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
'''
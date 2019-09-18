class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


'''
Runtime: 80 ms, faster than 94.74% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.4 MB, less than 5.72% of Python3 online submissions for Transpose Matrix.
'''